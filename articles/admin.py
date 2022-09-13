from django.contrib import admin
from .models import Articles,Categories,Comments, Images, News, Videos 

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    readonly_fields=['approver']
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'available', None) is True:
            obj.approver = request.user
            obj.save()
                    
admin.site.register(Images)


@admin.register(News)
class Newsdmin(admin.ModelAdmin):
    readonly_fields=['writer','last_edit_news']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields=['writer','last_edit_news']
        if obj:
            if not request.user.has_perm('news.editor_operations'):
                readonly_fields.append('available')
        return readonly_fields

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit_news = request.user
            obj.save()

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    readonly_fields=['writer','last_edit_video']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields=['writer','last_edit_video']
        if obj:
            if not request.user.has_perm('videos.editor_operations'):
                readonly_fields.append('available')
        return readonly_fields

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit_video = request.user
            obj.save()

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields=['writer','last_edit']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields=['writer','last_edit']
        if obj:
            if not request.user.has_perm('articles.editor_operations'):
                readonly_fields.append('available')
        return readonly_fields

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit = request.user
            obj.save()