from cgi import print_arguments
from .models import Categories,Comments, Videos,News,Articles
from settings import models
from .helpers import get_articles_sidebar

def categories_renderer(request):
    
    settings = models.Setting.objects.last()
    comms = Comments.objects.order_by('-id')[:3]
    videos = Videos.objects.filter(available=True).order_by('-id')[:3]

    article_list = get_articles_sidebar()
    print(article_list)
    categories = Categories.objects.all()

    return { 'all_categories': categories, 'sidebar_videos': videos, 'sidebar_news': article_list, 'sidebar_comms': comms, 'settings': settings}