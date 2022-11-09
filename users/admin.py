from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Rank, RankRequest, RankSub

class AccountAdmin(UserAdmin):
    list_display = ('username', 'last_login','cv','profile_activate','birthday','gender','description','image','facebook','twitter','instagram','youtube','github','website','linkedin','rank','rank_sub')
    list_filter = ()
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] += ('birthday','cv','profile_activate','gender','description','image','facebook','twitter','instagram','youtube','github','website','linkedin','rank','rank_sub')


admin.site.register(Account, UserAdmin)

admin.site.register(RankSub)

admin.site.register(Rank)

@admin.register(RankRequest)
class RankRequestAdmin(admin.ModelAdmin):
    readonly_fields=['approver']
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'available', None) is True:
            obj.approver = request.user
            obj.save()


    list_display = ('title','created_date','available')
    list_filter = ('title','created_date','available')