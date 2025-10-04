import platform
import os
from . import settings
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do_api.settings')

app = Celery('to_do_api')

if platform.system() == 'Windows':
    app.conf.pool = 'solo'
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    