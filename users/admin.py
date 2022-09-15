from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('username', 'last_login','cv','profile_activate','birthday','gender','description','image','facebook','twitter','instagram','youtube','github','website','linkedin')
    list_filter = ()
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] += ('birthday','cv','profile_activate','gender','description','image','facebook','twitter','instagram','youtube','github','website','linkedin')


admin.site.register(Account, UserAdmin)