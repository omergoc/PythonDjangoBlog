from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.shortcuts import render
from articles.models import Articles
from settings.models import Setting
from django.contrib import messages
from .models import Slider
from django.shortcuts import redirect
from .forms import ContactForm



def care(request):
    return render(request, 'care.html')

def care_control(function):
    def wrap(request, *args, **kwargs):
        settings = Setting.objects.last()
        if settings.available == True:
            return care(request, *args, **kwargs)
        else:
            return function(request, *args, **kwargs)
    return wrap


def handler404(request, exception=None):
    return render(request, '404.html')

    

@care_control
def index(request):
    slider_article = Slider.objects.order_by('-id')[:2]
    last_articles = Articles.objects.order_by('-id')[:10]
    context = {
        'articles': last_articles,
        'slider_article': slider_article
    }
    return render(request, 'index.html', context)


@care_control
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():       
            form.save()
            messages.success(request, "İşlem Başarılı...")
            return redirect(index)
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html',context)

@care_control
def services(request):
    return render(request, 'services.html')

@care_control
def brand(request):
    return render(request, 'brands.html')

@care_control
def about(request):
    return render(request, 'about.html')

@care_control
def not_found_404(request,exception):
    return render(request, '404.html')

@care_control
def favorites(request):
    article_list = Articles.objects.annotate(num_likes=Count('likedarticle')).filter(num_likes__gte=1)
    paginator = Paginator(article_list, 4) 

    page = request.GET.get('sayfa')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        'articles':articles
    }
    return render(request, 'favorites.html', context)
    
@care_control
def trend(request):
    article_list = Articles.objects.order_by('-views')

    paginator = Paginator(article_list, 4) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    context = {
        'articles':articles
    }
    return render(request, 'trends.html', context)