from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Writers
from articles.models import Articles
from settings.models import Setting


def care(request,writers_slug):
    return render(request, 'care.html')


def care_control(function):
    def wrap(request, *args, **kwargs):
        settings = Setting.objects.last()
        if settings.available == True:
            return care(request, *args, **kwargs)
        else:
            return function(request, *args, **kwargs)
    return wrap


@care_control
def index(request,writers_slug):
    writers = Writers.objects.get(slug=writers_slug)
    writer_id = writers.id
    
    article_list = Articles.objects.filter(author=writer_id ).all()
    paginator = Paginator(article_list, 5) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    context={
        'writer':writers,
        'author_articles':articles
    }
    return render(request, 'author.html',context)

    