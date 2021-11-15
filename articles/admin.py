from django.contrib import admin
from .models import Articles,Categories,Comments, Images


admin.site.register(Comments)

admin.site.register(Images)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('title',)}

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}