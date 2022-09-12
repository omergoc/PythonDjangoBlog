from django.shortcuts import render,redirect
from users.models import Account
from settings.models import Setting
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from articles.models import Articles
from django.contrib.auth import login, authenticate,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

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

@care_control
def loginUser(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():       
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, "Kullanıcı Adı Yada Şifre Hatalı")
            return redirect(loginUser)
    
        messages.success(request, "Giriş Başarılı...")
        login(request,user)
        return redirect("index")

    context = {
        'form': form
    }
    return render(request, 'login.html',context)

@care_control
def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():       
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        new_user = Account(username=username, first_name=first_name, last_name= last_name, email = email)
        new_user.set_password(password)
        new_user.save()
        login(request,new_user)
        messages.success(request, "Kayıt Başarılı...")
        return redirect("index")

    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html',context)

@care_control
def userLogout(request):
    logout(request)
    messages.success(request, "Çıkış Başarılı...")
    return redirect("index")

@care_control
def index(request,writers_slug):

    writers = get_object_or_404(Account, slug=writers_slug)
    writer_id = writers.id

    article_list = Articles.objects.filter(writer=writer_id ).all()
    print(article_list)
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

@care_control
def profile(request):
    return render(request, 'profile.html')

@care_control
def writers(request):

    User = get_user_model()
    writers_list = User.objects.all().filter(is_staff=True)
    paginator = Paginator(writers_list, 5) # Show 25 contacts per page

    page = request.GET.get('sayfa')
    try:
        writers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        writers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        writers = paginator.page(paginator.num_pages)

    context={
        'writers_list':writers
    }
    return render(request, 'writers.html',context)