from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render
from articles.models import Articles,News,Videos,Categories
from users.models import Account
from settings.models import Setting
from django.contrib import messages
from .models import Slider
from django.shortcuts import redirect
from .forms import ContactForm
from .helpers import mostliked_list, get_articles_list, get_viewcount, date_convert, articles_list_json

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

def handler500(request, exception=None):
    return render(request, "500.html")

@care_control
def index(request):
    slider_article = Slider.objects.order_by('-id')[:2]
    context = {
        'slider_article': slider_article
    }
    return render(request, 'index.html', context)

def get_category(id):
    category = Categories.objects.get(id=id)
    category_data ={
        'name':category.name,
        'slug':category.slug
    }
    return category_data

def get_writer(id):
    writer = Account.objects.get(id=id)
    writer_data ={
        'first_name':writer.first_name,
        'last_name':writer.last_name,
        'slug':writer.slug
        }
    return writer_data

@care_control
def PostJsonListView(request, id):
        data_list = []
        upper = id
        lower = upper - 5
        articles = articles_list_json()
        for article in articles:
            data = {
                'view_count':article['view_count'],
                'id': article['id'],
                'category_title':article['category_name'],
                'category_slug':article['category_slug'],
                'writer_name': article['name'],
                'writer_slug': article['name_slug'],
                'article_created_date':date_convert(article['created_date'].strftime("%d/%m/%Y %H:%M")),
                'article_image':article['image'],
                'article_title':article['title'],
                'article_slug':article['slug'],
                'article_content':article['description'],
            }
            data_list.append(data)
        posts_size = len(data_list)
        posts = data_list[lower:upper]
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)

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
def dashboard(request,exception):
    return render(request, 'dashboard.html')

@care_control
def favorites(request):
    article_list = mostliked_list()
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
    article_list = get_articles_list()

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
    return render(request, 'trends.html', context)