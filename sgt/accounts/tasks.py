from __future__ import absolute_import

from sgt.accounts.utils import create_payment
from sgt.accounts.models import UserDbv
from sgt.celery import app


@app.task
def task_payments(ignore_result=True, name="task_payments"):
    for d in UserDbv.objects.all():
        create_payment(d.pk)
