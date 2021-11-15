from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CommentsForm
from .models import Categories, Articles,Comments
from settings.models import Setting


def care(request,categories_slug):
    return render(request, 'care.html')

def care_control(function):
    def wrap(request, *args, **kwargs):
        settings = Setting.objects.last()
        if settings.available == True:
            return care(request, *args, **kwargs)
        else:
            return function(request, *args, **kwargs)
    return wrap


def care2(request,categories_slug,articles_slug):
    return render(request, 'care.html')

def care_control2(function):
    def wrap(request, *args, **kwargs):
        settings = Setting.objects.last()
        if settings.available == True:
            return care(request, *args, **kwargs)
        else:
            return function(request, *args, **kwargs)
    return wrap


@care_control
def category(request,categories_slug):
    
    category = Categories.objects.get(slug=categories_slug)
    category_id = category.id
    article_list = Articles.objects.filter(category=category_id)
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
    context = {
        'articles':articles,
        'category':category
    }
    return render(request ,'category.html',context)

@care_control2
def article(request,categories_slug,articles_slug):
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            article = Articles.objects.filter(slug = articles_slug).first()            
            post = form.save(commit=False)
            post.article=article
            post.save()
            messages.success(request,"İşlem Başarılı...")
            return redirect('/')
    else:
        form = CommentsForm()
        category = Categories.objects.get(slug=categories_slug)
        category_id = category.id
        article = Articles.objects.filter(slug = articles_slug, category=category_id).first()
        new_views= article.views +1
        article_update =Articles.objects.get(id=article.id)
        article_update.views=new_views 
        article_update.save()
        comments= Comments.objects.filter(article=article,available=True).all()
        count = comments.count()
        context = {
            'article': article,
            'form':form,
            'comments':comments,
            'count':count
        
        }
        return render(request ,'article.html',context)
