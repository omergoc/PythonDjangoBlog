from django.shortcuts import render,redirect
from users.models import Account
from settings.models import Setting
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from articles.models import Articles
from django.contrib.auth import login, authenticate,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str    
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string  
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage  


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
        is_active = False
        new_user = Account(username=username, first_name=first_name, last_name= last_name, email = email, is_active=is_active)
        new_user.set_password(password)
        new_user.save()

        current_site = get_current_site(request)  
        mail_subject = 'Activation link has been sent to your email id'  
        message = render_to_string('acc_active_email.html', {  
            'user': new_user,  
            'domain': current_site.domain,  
            'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),  
            'token':account_activation_token.make_token(new_user),  
        })  
        to_email = form.cleaned_data.get('email')  
        email = EmailMessage(  
                    mail_subject, message, to=[to_email]  
        )  
        email.send()  
        return render(request, 'Email.html',{'msg':'Kaydı tamamlamak için lütfen e-posta adresinizi onaylayın'})  
        

    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html',context)
    

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True
        user.save()  
        return render(request,'Email.html',{'msg':'E-posta onayınız için teşekkür ederiz. Artık hesabınıza giriş yapabilirsiniz.'})  
    else:  
        return render(request, 'Email.html',{'msg':'Aktivasyon bağlantısı geçersiz!'})  


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