from sgt.core.models import Payment
from sgt.accounts.models import UserDbv
from datetime import datetime


def create_payment(pk):
    """
        Mudar a lógica para a situação onde o desbravador
        tenha pago a última mensalidade. Sendo assim, deve-ser
        verificar se há alguma mensalidade não paga, ao invés
        de só a última.
    """
    dbv = UserDbv.objects.get(pk=pk)
    if dbv.is_debtor():
        new = Payment.objects.create(
            month=datetime.now(), dbv=dbv
        )
        new.save()
        print(new)
    else:
        print("não devedor")
