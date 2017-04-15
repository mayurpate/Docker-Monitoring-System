
from mongoengine import *
from datetime import datetime

connect(db = 'docstats', host = 'localhost', port = 27017)

class MonitoringStats(Document):
    ip_address = StringField(default = None)
    containers = ListField(DictField(default = {}))
    machine = DictField(default = {})
    created_at = DateTimeField(default = datetime.now)
    

