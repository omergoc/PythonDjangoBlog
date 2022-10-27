from os import read
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Categories, Articles,Comments,LikedArticle, Videos, News,ReadPost
from users.models import Account
from settings.models import Setting
from django.http import Http404
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

@care_control
def articles(request):
    article_list = Articles.objects.all().filter(available=True)
    paginator = Paginator(article_list, 5) 

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

def read_save(read_id, post_id):
    control = ReadPost.objects.filter(read_id = read_id, post=post_id).last()
    if control == None:
        like, created = ReadPost.objects.get_or_create(read_id = read_id, post=post_id)


@care_control2
def article(request,categories_slug,articles_slug):
    user = request.user.id if request.user.id else 0

    if request.method == "POST":
        return redirect(request.META['HTTP_REFERER'])
    else:
        category = Categories.objects.get(slug=categories_slug)
        category_id = category.id

        article = Articles.objects.filter(slug = articles_slug, category=category_id,available=True).first()
        video = Videos.objects.filter(slug = articles_slug, category=category_id,available=True).first()
        news = News.objects.filter(slug = articles_slug, category=category_id,available=True).first()

        if request.user.is_anonymous:
            global has_key
            has_key = request.session.get('cached_session_key', None)
            if has_key is None:
                if not request.session.session_key:
                    request.session.save()
                request.session['cached_session_key'] = request.session.session_key
        if not request.session.session_key:
            request.session.save()
            request.session['cached_session_key'] = request.session.session_key
        read_id = request.session['cached_session_key']

        if video:
            data = video
            read_save(read_id, post_id=data.id)
            comments= Comments.objects.filter(videos=data,available=True).all()
            count = comments.count()
            control_like = LikedArticle.objects.filter(user_id = user, post=data.id).last()
            control_like = control_like.status if control_like != None else 0
            context = { 'video': data, 'comments':comments,'count':count,'control_like':control_like}
            response = render(request ,'video.html',context)
            return response

        elif article:
            data = article
            read_save(read_id, post_id=data.id)
            comments= Comments.objects.filter(article=data,available=True).all()
            count = comments.count()
            control_like = LikedArticle.objects.filter(user_id = user, post=data.id).last()
            control_like = control_like.status if control_like != None else 0
            context = { 'article': data, 'comments':comments,'count':count,'control_like':control_like}
            response = render(request ,'article.html',context)
            return response

        elif news:
            data = news
            read_save(read_id, post_id=data.id)
            comments= Comments.objects.filter(news=data,available=True).all()
            count = comments.count()
            control_like = LikedArticle.objects.filter(user_id = user, post=data.id).last()
            control_like = control_like.status if control_like != None else 0
            context = { 'new': data, 'comments':comments,'count':count,'control_like':control_like}
            response = render(request ,'new.html',context)
            return response
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
        if slug.strip() == '' or content.strip() == '' or type.strip() == '':
            return HttpResponse("None")

        username = request.user
        user = Account.objects.filter(username = username).first()
        created = False
        if 'makale' == type:
            article = Articles.objects.get(slug=slug)
            comment, created = Comments.objects.get_or_create(name=f"{user.first_name} {user.last_name}", email=user.email, content=content, article = article)
        
        if 'video' == type:
            article = Videos.objects.get(slug=slug)
            comment, created = Comments.objects.get_or_create(name=f"{user.first_name} {user.last_name}", email=user.email, content=content, videos = article)
        
        if 'haber' == type:
            article = News.objects.get(slug=slug)
            comment, created = Comments.objects.get_or_create(name=f"{user.first_name} {user.last_name}", email=user.email, content=content, news = article)

        if created:
            return HttpResponse("Başarılı Bir Şekilde Yorum Yaptınız")
        else:
            return HttpResponse("Yorumu Gönderirken Hata Oluştu")

