#!/usr/bin/env python

import requests
import json

CADVISOR_URL = "http://localhost:8080/api/v1.3/"
SERVER_URL = "http://localhost:5000/docker_controller/collect_stats"

if __name__ == "__main__":
    data = requests.get(url = "%s/docker" %CADVISOR_URL)
    
    all_stats = []
    for key,val in data.json().items():
        total_memory_usage = 0
        total_stats = len(val.get('stats'))
        for stat in val.get('stats'):
            total_memory_usage = total_memory_usage + (stat['memory']['usage'] / 1024.0)
        average_cpu_load = val['stats'][-1]['cpu']['usage']['total'] - val['stats'][0]['cpu']['usage']['total']
        if average_cpu_load <= 0:
            average_cpu_load = 0
        else:
            average_cpu_load = float(average_cpu_load) / 1000000000
        average_memory_usage = total_memory_usage / total_stats

        all_stats.append({'id': val['id'],
                        'name': val['aliases'][0],
                        'creation_time': val['spec']['creation_time'],
                        'image': val['spec']['image'],
                        'average_cpu_load': float(average_cpu_load) / 100,
                        'average_memory_usage': average_memory_usage,
                        'timestamp': val['stats'][0]['timestamp'] 
                    })
    final_info = {}
    machine = requests.get(url = "%s/machine" %CADVISOR_URL)
    final_info['machine'] = machine.json()
    final_info['container_stat'] = all_stats

    headers = {'content-type': 'application/json'}
    post_result = requests.post(url = SERVER_URL, data=json.dumps(final_info), headers=headers)

