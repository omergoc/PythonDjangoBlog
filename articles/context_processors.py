from .models import Categories,Comments, Videos, News
from settings import models


def categories_renderer(request):
    
    settings = models.Setting.objects.last()
    comms = Comments.objects.order_by('-id')[:3]
    videos = Videos.objects.filter(available=True).order_by('-id')[:3]
    news = News.objects.filter(available=True).order_by('-id')[:3]
    news = Categories.objects.filter(name="Siberatay Haberleri").order_by('-id')[:3]
    categories = Categories.objects.all()

    return { 'all_categories': categories, 'sidebar_videos': videos, 'sidebar_news': news, 'sidebar_comms': comms, 'settings': settings}