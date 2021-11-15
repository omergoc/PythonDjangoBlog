from functools import wraps
from .models import Categories,Articles,Comments
from settings import models

def categories_renderer(request):
    articles = Articles.objects.order_by('-views')[:3]
    settings = models.Setting.objects.last()
    comms = Comments.objects.order_by('-id')[:3]
    return {'all_categories': Categories.objects.all(),'sidebar_articles':articles,'sidebar_comms':comms,'settings':settings}