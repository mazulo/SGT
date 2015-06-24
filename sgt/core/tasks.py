from __future__ import absolute_import
from core.models import Desbravador, Mensalidade
from datetime import datetime
from sgt.celery import app


@app.task(ignore_result=True)
def verifica_mensalidade():
    """
        Mudar a lógica para a situação onde o desbravador
        tenha pago a última mensalidade. Sendo assim, deve-ser
        verificar se há alguma mensalidade não paga, ao invés
        de só a última.
    """
    dbvs = Desbravador.objects.all()
    for dbv in dbvs:
        if not dbv.mensalidades.latest('pk').status_pagamento:
            nova_mesalidade = Mensalidade(mes=datetime.now(), desbravador=dbv)
            nova_mesalidade.save()
