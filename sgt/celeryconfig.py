from datetime import timedelta

BROKER_URL = 'amqp://guest:guest@localhost:5672//'

CELERY_TIMEZONE = 'America/Fortaleza'

CELERY_ALWAYS_EAGER = False

CELERYBEAT_SCHEDULE = {
    'payments': {
        'task': 'sgt.accounts.tasks.task_payments',
        'schedule': timedelta(seconds=30),
        'args': ()
    }
}
