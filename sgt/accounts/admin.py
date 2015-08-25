from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserDbv
from sgt.core.models import Payment
from .forms import CustomUserDbvChangeForm, CustomUserDbvCreationForm


class PaymentAdmin(admin.TabularInline):

    model = Payment
    extra = 0

    def has_add_permission(self, request):
        return True


class UserDbvAdmin(UserAdmin):

    form = CustomUserDbvChangeForm
    add_form = CustomUserDbvCreationForm
    inlines = [
        PaymentAdmin
    ]
    list_display = (
        'username', 'email', 'is_staff', 'is_superuser', 'is_debtor'
    )
    list_filter = ('is_superuser',)

    fieldsets = (
        (
            None,
            {'fields': (
                'username',
                'email',
                'password',
                'first_name',
                'last_name',
                'age',
                'profile_image',
                'team',
                'position')}
        ),
        (
            'Permissions',
            {'fields': ('is_active', 'is_superuser', 'is_staff')}
        )
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username', 'email',
                    'password1', 'password2',
                    'is_staff', 'is_superuser'
                )
            }
        ),
    )

    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(UserDbv, UserDbvAdmin)
