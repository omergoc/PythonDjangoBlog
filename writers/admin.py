from django.contrib import admin
from .models import Writers

@admin.register(Writers)
class WritersAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('author',)}
