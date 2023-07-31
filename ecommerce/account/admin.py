from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from .forms import UserChangeForm , UserCreationForm
from .models import CustomUser

#To  make a form in admin.py for Admin panel
class CustomUserAdmin(UserAdmin):
    # This form  adds and changes user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name','family','mobile_number','gender','is_active', 'is_admin')
    list_filter = ('is_admin',) #???????????????????
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','family','mobile_number','gender')}),
        ('Permissions', {'fields': ('is_active','is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name','family','mobile_number','gender','is_active', 'is_admin', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',) #??????????????
    filter_horizontal = () #????????????????


# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


