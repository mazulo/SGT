from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserDbv
from .forms import CustomUserDbvChangeForm, CustomUserDbvCreationForm


class UserDbvAdmin(UserAdmin):

    form = CustomUserDbvChangeForm
    add_form = CustomUserDbvCreationForm

    list_display = ('username', 'email', 'is_staff', 'is_superuser')
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
                'group',
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
