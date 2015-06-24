from django.contrib import admin
from sgt.core.models import Unidade, Mensalidade


class MensalidadeInline(admin.TabularInline):
    model = Mensalidade
    extra = 0

    def has_add_permission(self, request):
        return True


@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'historia')


admin.site.register(Mensalidade)
