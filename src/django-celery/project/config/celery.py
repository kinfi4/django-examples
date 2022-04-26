import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('mailing_list')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-spam-every-5-minutes': {
        'task': 'mailing_list.tasks.send_spam_email',
        'schedule': crontab(minute='*/3')
    }
}
