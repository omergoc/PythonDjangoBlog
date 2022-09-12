from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('username', 'last_login','birthday','gender','description','image','facebook','twitter','instagram','youtube','github','website')
    list_filter = ()
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] += ('birthday','gender','description','image','facebook','twitter','instagram','youtube','github','website')


admin.site.register(Account, UserAdmin)