from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import MemberCreationForm, MemberChangeForm
from django.contrib.auth.admin import UserAdmin

#class MemberAdmin(admin.ModelAdmin):
#    add_form = MemberCreationForm
#    form = MemberCreationForm
#    model = Member
#    list_display = [
#        'email',
#        'username',
#        'date_of_birth',
#        'graduation_year',
#        'specialized']


class MemberAdmin(UserAdmin):
    form = MemberChangeForm
    add_form = MemberCreationForm
    list_display = [
        'email',
        'username',
        'date_of_birth',
        'graduation_year',
        'specialized'
    ]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', )}),
        ('Permissions', {'fields': ('user_permissions', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'graduation_year', 'specialized', 'password')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Register your models here.
admin.site.register(get_user_model(), MemberAdmin)
