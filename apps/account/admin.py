from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserToken
from .forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser', 'modified_date', 'created_date', 'verify_date')
    date_hierarchy = 'created_date'
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'modified_date', 'created_date')}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    readonly_fields = ('last_login', 'modified_date', 'created_date')
    search_fields = ("email",)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    # filter_horizontal = ('groups', 'user_permissions')
    list_editable = ('is_active', 'is_staff', 'is_superuser')
    ordering = ()


@admin.register(UserToken)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_used', 'token', 'created_date')
    date_hierarchy = 'created_date'
    list_filter = ('is_used', )
    search_fields = ('user__username', 'token',)


admin.site.index_title = 'Abiturient Admin'
admin.site.site_header = 'Abiturient Administration'
