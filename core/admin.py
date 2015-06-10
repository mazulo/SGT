from django.contrib import admin
from core.models import Desbravador, Unidade, Mensalidade


class MensalidadeInline(admin.TabularInline):
    model = Mensalidade
    extra = 0

    def has_add_permission(self, request):
        return True


@admin.register(Desbravador)
class DesbravadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'unidade', 'cargo')
    list_filter = ('nome', 'unidade')
    inlines = [MensalidadeInline, ]


@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'historia')


admin.site.register(Mensalidade)
