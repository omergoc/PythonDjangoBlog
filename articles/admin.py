from django.contrib import admin
from .models import Articles,Categories,Comments, Images, News, Videos 

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields ={'slug':('name',)}

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    readonly_fields=['approver']
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'available', None) is True:
            obj.approver = request.user
            obj.save()
    def Comment_Preview(self,obj):
        if(len(obj.content)>=150):
            return obj.content[:147]+"..."
        else:
            return obj.content
    
    def get_sub_title(self, obj):
        if obj.article:
            return obj.article
        elif obj.news:
            return obj.news
        elif obj.videos:
            return obj.videos       
        else:
            return 'Not Available'

    list_display = ('get_sub_title','Comment_Preview','name','created_date','available')
    list_filter = ('videos','article','news','name','created_date','available')

    get_sub_title.short_description = 'Konu'
    Comment_Preview.short_description = 'Yorum içerik'

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image_name',)
    list_filter = ('image_name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    readonly_fields=['writer','last_edit_news','available','types']
    list_display = ('title','writer','last_edit_news','created_date','available')
    list_filter = ('title','writer','last_edit_news','created_date','available')

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
    list_display = ('title','writer','last_edit_video','created_date','available')
    list_filter = ('title','writer','last_edit_video','created_date','available')

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
    list_display = ('title','writer','last_edit','created_date','available')
    list_filter = ('title','writer','last_edit','created_date','available')

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
    
    