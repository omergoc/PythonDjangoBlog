from http.client import HTTPResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponse
from .models import Categories, Articles,Comments,LikedArticle, Videos, News
from blogapp.settings import base
from users.models import Account
from settings.models import Setting
from django.http import Http404
from django.db import connection
import datetime


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

def set_cookie(response, key, value, days_expire=1):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=base.SESSION_COOKIE_DOMAIN,
        secure=base.SESSION_COOKIE_SECURE or None,
    )

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
        "type":"makale",
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
        "type":"haber",
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
        "type":"video",
        "name": "Videolar",
        "description": "Tüm Videolar"
    }
    context = {
        'articles':videos,
        'category':category_types
    }
    return render(request, 'category.html',context)

def sql_test_code(id):
    #raw sql query here
    query = f"""
        SELECT * FROM articles_articles INNER JOIN articles_categories ON articles_categories.id = {id} 
        INNER JOIN
        articles_videos
        ON
        articles_videos.category_id = {id}
        INNER JOIN
        articles_news
        ON
        articles_news.category_id = {id}"""
    
    #a cursor object
    with connection.cursor() as cursor:
        #execute the query
        cursor.execute(query)
        #get all the rows as a list
        rows = cursor.fetchall()
    return rows

@care_control
def category(request,categories_slug):
    category_types = None
    try:
        category = Categories.objects.get(slug=categories_slug)
    except Categories.DoesNotExist:
        raise Http404("404 Not Found | Aradığınız Sayfa Bulunamadı.")

    category = Categories.objects.get(slug=categories_slug)
    category_id = category.id
    article_list = list(Articles.objects.filter(category=category_id,available=True))
    video_list = list(Videos.objects.filter(category=category_id,available=True))
    new_list = list(News.objects.filter(category=category_id,available=True))
    article_list = article_list + new_list + video_list
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
        user = request.user.id if request.user.id else 0
        
        if video:
            data = video
            comments= Comments.objects.filter(article=article,available=True).all()
            count = comments.count()
            control_like = LikedArticle.objects.filter(user_id = user, post=data.id).last()
            control_like = control_like.status if control_like != None else 0
            context = { 'video': data, 'comments':comments,'count':count,'control_like':control_like}
            return render(request ,'video.html',context)

        elif article:
            bookname = request.COOKIES if 'bookname' in request.COOKIES else None
            data = article
            comments= Comments.objects.filter(article=article,available=True).all()
            count = comments.count()
            control_like = LikedArticle.objects.filter(user_id = user, post=data.id).last()
            control_like = control_like.status if control_like != None else 0
            context = { 'article': data, 'comments':comments,'count':count,'control_like':control_like}
            response = render(request ,'article.html',context)
            response.set_cookie('bookname','Sherlock Holmes',max_age=1)
            return response

        elif news:
            data = news
            comments= Comments.objects.filter(article=article,available=True).all()
            count = comments.count()
            control_like = LikedArticle.objects.filter(user_id = user, post=data.id).last()
            control_like = control_like.status if control_like != None else 0
            context = { 'new': data, 'comments':comments,'count':count,'control_like':control_like}
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
            status = True
            like, created = LikedArticle.objects.get_or_create(user=request.user, post = id,status=status)

        if status:
            return HttpResponse("İlgili İçeriği Beğendiniz")
        else:
            return HttpResponse("İlgili İçeriği Beğenmekten Vazgeçtiniz")


def article_comment(request):
    if request.method == 'POST':
        type = request.POST['type']
        content = request.POST['content']
        slug = request.POST['slug']
        username = request.user
        user = Account.objects.filter(username = username).first()
        created = False
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

