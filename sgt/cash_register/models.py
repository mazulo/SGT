from django.db import models


class CashValue(models.Model):

    TYPES = (
        (
            ('M', 'Mensalidade'),
            ('D', 'Doações'),
            ('A', 'Entrada Avulsa'),
        ),
        (
            ('C', 'Compra de Materiais'),
            ('S', 'Pagamento Seguro'),
        )
    )

    cash_value = models.DecimalField(
        'Valor',
        max_digits=8,
        decimal_places=2
    )
    date_value = models.DateField('Data', auto_now_add=True)
    # type_
    description = models.TextField('Descrição', blank=True)
    cash_flow = models.ForeignKey(
        'CashFlow',
        verbose_name='Caixa',
        related_name="%(app_label)s_%(class)s_flow"
    )

    class Meta:
        abstract = True

    def __str__(self):
        self.cash_value


class CashInput(CashValue):

    _type = models.CharField('Tipo de Entrada', choices=CashValue.TYPES[0])

    class Meta:
        verbose_name = "Entrada de Dinheiro"
        verbose_name_plural = "Entradas de Dinheiro"


class CashOutput(CashValue):

    _type = models.CharField('Tipo de Entrada', choices=CashValue.TYPES[1])

    class Meta:
        verbose_name = "Saída de Dinheiro"
        verbose_name_plural = "Saídas de Dinheiro"


class CashFlow(models.Model):

    total_values = models.DecimalField(
        'Valor',
        max_digits=8,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Fluxo de Caixa"
        verbose_name_plural = "Fluxos de Caixa"

    def __str__(self):
        pass
