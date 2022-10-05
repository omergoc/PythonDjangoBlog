from .models import Categories,Comments, Videos,News,Articles
from settings import models


def categories_renderer(request):
    
    settings = models.Setting.objects.last()
    comms = Comments.objects.order_by('-id')[:3]
    videos = Videos.objects.filter(available=True).order_by('-id')[:3]
    category = Categories.objects.get(name="Siberatay Haberleri")
    article_list = list(Articles.objects.filter(category=category.id,available=True).order_by('-id')[:1])
    video_list = list(Videos.objects.filter(category=category.id,available=True).order_by('-id')[:1])
    new_list = list(News.objects.filter(category=category.id,available=True).order_by('-id')[:1])
    article_list = article_list + new_list + video_list
    categories = Categories.objects.all()

    return { 'all_categories': categories, 'sidebar_videos': videos, 'sidebar_news': article_list, 'sidebar_comms': comms, 'settings': settings}