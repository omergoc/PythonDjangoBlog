from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Categories, Articles,Comments,LikedArticle, Videos, News
from users.models import Account
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
def articles(request):

    article_list = Articles.objects.all().filter(available=True)
    paginator = Paginator(article_list, 5) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    category_types =  {
        "name": "Makaleler",
        "description": "Tüm Makaleler"
    }
    context = {
        'articles':articles,
        'category':category_types
    }
    return render(request, 'category.html',context)


@care_control
def news(request):

    news_list = News.objects.all().filter(available=True)
    paginator = Paginator(news_list, 5) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    category_types =  {
        "name": "Haberler",
        "description": "Tüm Haberler"
    }
    context = {
        'articles':news,
        'category':category_types
    }
    return render(request, 'category.html',context)

@care_control
def videos(request):

    video_list = Videos.objects.all().filter(available=True)
    paginator = Paginator(video_list, 5) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)
    category_types =  {
        "name": "Videolar",
        "description": "Tüm Videolar"
    }
    context = {
        'articles':videos,
        'category':category_types
    }
    return render(request, 'category.html',context)

@care_control
def category(request,categories_slug):
    category_types = None

    category = Categories.objects.get(slug=categories_slug)
    category_id = category.id
    article_list = Articles.objects.filter(category=category_id,available=True)
    category_types = category
        
    paginator = Paginator(article_list, 4) 

    page = request.GET.get('sayfa')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {
        'articles':articles,
        'category':category_types
    }
    return render(request ,'category.html',context)

@care_control2
def article(request,categories_slug,articles_slug):
    if request.method == "POST":
        return redirect(request.META['HTTP_REFERER'])
    else:
        category = Categories.objects.get(slug=categories_slug)
        category_id = category.id

        article = Articles.objects.filter(slug = articles_slug, category=category_id,available=True).first()
        video = Videos.objects.filter(slug = articles_slug, category=category_id,available=True).first()
        news = News.objects.filter(slug = articles_slug, category=category_id,available=True).first()
        if video:
            data = video
            comments= Comments.objects.filter(article=article,available=True).all()
            count = comments.count()
            context = { 'video': data, 'comments':comments,'count':count}
            return render(request ,'video.html',context)

        elif article:
            data = article
            comments= Comments.objects.filter(article=article,available=True).all()
            count = comments.count()
            context = { 'article': data, 'comments':comments,'count':count}
            return render(request ,'article.html',context)

        elif news:
            data = news
            comments= Comments.objects.filter(article=article,available=True).all()
            count = comments.count()
            context = { 'new': data, 'comments':comments,'count':count}
            return render(request ,'new.html',context)
        else:
            return redirect(request.META['HTTP_REFERER'])


def article_like(request):
    if request.method == 'POST':
        id = request.POST['id']
        user = Account.objects.filter(username = request.user).first()
        user_id = user.id

        control = LikedArticle.objects.filter(user_id = user_id, post=id).last()

        if control:
            status = False if control.status == True else True
            like, created = LikedArticle.objects.update_or_create(id=control.id, user=request.user, post = id, defaults={'status':status})
        else:
            like, created = LikedArticle.objects.get_or_create(user=request.user, post = id,status=True)

        if created:
            return HttpResponse("True")
        else:
            return HttpResponse("Flase")


def article_comment(request):
    if request.method == 'POST':
        type = request.POST['type']
        content = request.POST['content']
        slug = request.POST['slug']
        username = request.user
        user = Account.objects.filter(username = username).first()

        if 'makale' in type:
            article = Articles.objects.get(slug=slug)
            comment, created = Comments.objects.get_or_create(name=f"{user.first_name} {user.last_name}", email=user.email, content=content, article = article)
        
        if 'video' in type:
            article = Videos.objects.get(slug=slug)
            comment, created = Comments.objects.get_or_create(name=f"{user.first_name} {user.last_name}", email=user.email, content=content, article = article)
        
        if 'haber' in type:
            article = News.objects.get(slug=slug)
            comment, created = Comments.objects.get_or_create(name=f"{user.first_name} {user.last_name}", email=user.email, content=content, article = article)

        if created:
            return HttpResponse("True")
        else:
            return HttpResponse("Flase")

