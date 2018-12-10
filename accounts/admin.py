from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member, SuperAdmin
from .forms import MemberCreationForm


class MemberAdmin(admin.ModelAdmin):
    add_form = MemberCreationForm
    form = MemberCreationForm
    model = Member
    list_display = [
        'email',
        'username',
        'date_of_birth',
        'graduation_year',
        'specialized']


# Register your models here.
admin.site.register(Member, MemberAdmin)
admin.site.register(SuperAdmin, MemberAdmin)
