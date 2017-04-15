import logging
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from docker_monitoring.lib.base import BaseController, render

from docker_monitoring.model import *

log = logging.getLogger(__name__)

class DockerControllerController(BaseController):

    def index(self):
        return 'Hello World'

    def collect_stats(self):
        stats = json.loads(request.body, encoding=request.charset)
        log.info("Objects:%s" %len(MonitoringStats.objects()))
        
        m = MonitoringStats(ip_address = request.environ['REMOTE_ADDR'],
                            containers = stats.get('container_stat'),
                            machine = stats.get('machine'))
        m.save()
        log.info("Stats:%s" %stats)
        res = {'status': 200}
        return json.dumps(res)

    def get_host_details(self):
        res = {'success': True}
        host_ip = request.params.get('host_ip', '127.0.0.1')
        stats = MonitoringStats.objects(ip_address = host_ip)
        if stats:
            m = stats[0]['machine']
            c = stats[0]['containers']
            res.update({'machine_info': [{'k': 'Number of Cores', 'v': m['num_cores']},
                                        {'k': 'CPU Frequency (KHZ)', 'v': m['cpu_frequency_khz']},
                                        {'k': 'System UUID', 'v': m['system_uuid']},
                                        {'k': 'MAC Address', 'v': m['network_devices'][0]['mac_address']},
                                        {'k': 'Memory Capacity (MB)', 'v': ((m['memory_capacity'] / 1024)/1024)}]
                        })
            res.update({'containers': []})
            for container in c:
                res['containers'].append({'name': container['name'],'image': container['image'],
                                        'id': container['id']})
        else:
            res['success'] = False
        return json.dumps(res)

    def get_container_details(self):
        from datetime import datetime
        res = {'success': True}
        container_id = request.params.get('container_id')
        hr_min = []
        cpu_stats = []
        memory_stats = []
        for stat in MonitoringStats.objects(containers__id = container_id)[0:10]:
            hr_min.append(stat['created_at'].strftime('%H:%M'))
            for c in stat['containers']:
                if c.get('id') == container_id:
                    cpu_stats.append(c.get('average_cpu_load'))
                    memory_stats.append(c.get('average_memory_usage'))

        log.info("Time:%s" %hr_min)
        log.info("CPU Stats:%s" %cpu_stats)
        log.info("Mem Stats:%s" %memory_stats)
        log.info("Container ID:%s" %container_id)
        res.update({'time_series': hr_min,
                    'cpu_stats': cpu_stats,
                    'memory_stats': memory_stats})
        return json.dumps(res)
    
