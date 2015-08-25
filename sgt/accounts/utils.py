from sgt.core.models import Payment
from datetime import datetime


def create_payment(dbv):
    """
        Mudar a lógica para a situação onde o desbravador
        tenha pago a última mensalidade. Sendo assim, deve-ser
        verificar se há alguma mensalidade não paga, ao invés
        de só a última.
    """
    if dbv.is_debtor():
        new = Payment.objects.create(
            month=datetime.now(), dbv=dbv
        )
        new.save()
        print(new)
    else:
        print("não devedor")
