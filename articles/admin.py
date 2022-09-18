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
    readonly_fields=['writer','last_edit_news','available','types']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields=['writer','last_edit_news','available','types']
        if obj:
            if request.user.groups.filter(name='Haber Editörü').exists():
                readonly_fields.remove('available')
                readonly_fields.remove('types')
        return readonly_fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(writer=request.user)
        
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit_news = request.user
            obj.save()

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    readonly_fields=['writer','last_edit_video','available','types']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields=['writer','last_edit_video','available','types']
        if obj:
            if request.user.groups.filter(name='Video Editörü').exists():
                readonly_fields.remove('available')
                readonly_fields.remove('types')
        return readonly_fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(writer=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit_video = request.user
            obj.save()

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields=['writer','last_edit','available','types']

    def get_readonly_fields(self, request, obj=None):
        readonly_fields=['writer','last_edit','available','types']
        if obj:
            if request.user.groups.filter(name='Makale Editörü').exists():
                readonly_fields.remove('available')
                readonly_fields.remove('types')
        return readonly_fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(writer=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit = request.user
            obj.save()
    
    