from django.contrib import admin
from .models import Contact, Slider



admin.site.register(Contact)


@admin.register(Slider)
class SlidersAdmin(admin.ModelAdmin):
    readonly_fields=['writer']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit = request.user
            obj.save()