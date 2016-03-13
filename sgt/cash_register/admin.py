from django.contrib import admin

from .models import CashInput, CashOutput


admin.site.register(CashInput)
admin.site.register(CashOutput)
