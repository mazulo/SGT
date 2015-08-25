from __future__ import absolute_import
from celery.task.schedules import crontab
from celery.decorators import periodic_task

from datetime import datetime
from sgt.accounts.utils import create_payment
from sgt.accounts.models import UserDbv


@periodic_task(
    run_every=(crontab()),
    name="create_payment",
    ignore_result=True
)
def create_payments():
    for d in UserDbv.objects.all():
        create_payment(d)
