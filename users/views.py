from django.shortcuts import render,redirect
from users.models import Account
from settings.models import Setting
from django.contrib import messages
from .forms import RegisterForm, LoginForm,UpdateUserForm
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
    if  request.user.username:
        return redirect("index")
        
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
    if  request.user.username:
        return redirect("index")

    form = RegisterForm(request.POST or None)
    if form.is_valid():       
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        try:
            control = Account.objects.get(username = username)
        except Account.DoesNotExist:
            control = None

        if control is  None:
            is_active = False
            new_user = Account(username=username, first_name=first_name, last_name= last_name, email = email, is_active=is_active)
            new_user.set_password(password)
            new_user.save()
            try:
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
                """
                login(request,new_user)
                messages.success(request, "Kayıt Başarılı...")
                return redirect("index")
                """
            except:
                messages.warning(request, "Bilinmedik Bir Hata Oluştu Lütfen Site Yöneticilerine Bildiriniz.")
                return redirect(loginUser) 

        else:
            messages.warning(request, "Kullanıcı Adı Daha Önce Kullanılmış.")
            return redirect(loginUser) 
        

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
    paginator = Paginator(article_list, 5) 

    page = request.GET.get('sayfa')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context={
        'writer':writers,
        'author_articles':articles
    }
    return render(request, 'author.html',context)

@care_control
def profile(request):
    if not request.user.username:
        return redirect("index")
    
    if request.method == 'POST':  
        
        slug =  request.user.slug    
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        birthday = request.POST['birthday']
        description = request.POST['description']
        facebook = request.POST['facebook']
        instagram = request.POST['instagram']
        twitter = request.POST['twitter']
        linkedin = request.POST['linkedin']
        github = request.POST['github']
        website = request.POST['website']
        profile_activate = 1 if request.POST.get('profile_activate', 0) == 'on' else 0
        

        if 'cv' in request.FILES:
            if str(request.FILES['cv'])[-3:] == 'pdf':
                cv = cv_upload(request.FILES['cv'], slug)
            else:
                messages.warning(request, "CV Bölümüne Sadece PDF Dosya Yükleyiniz...")
                return redirect("profile")
        else:
            cv = request.POST['old_cv']

        if 'image' in request.FILES:
            if str(request.FILES['image'])[-3:] == 'jpg':
                image = image_upload(request.FILES['image'], slug)

            else:
                messages.warning(request, "Profil Fotoğrafı Bölümüne Sadece jPG Dosya Yükleyiniz...")
                return redirect("profile")
        else:
            image = request.POST['old_image']

        try:
            Account.objects.filter(username=request.user.username).update(profile_activate=profile_activate, email=email, first_name=first_name, last_name=last_name, birthday=birthday,description=description, facebook=facebook, instagram=instagram, twitter=twitter, linkedin=linkedin, github=github, website=website,cv=cv,image=image)
            messages.success(request, "Güncelleme Başarılı...")
        except:
            messages.warning(request, "Hata Oluştu...")

        return redirect("profile")

    return render(request,'profile.html')


def cv_upload(f,slug): 
    path = 'static/upload/cv/'+slug+'.pdf'
    with open('static/upload/cv/'+slug+'.pdf', 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    return path


def image_upload(f,slug): 
    path = 'static/upload/author/'+slug+'.jpg'
    with open('static/upload/author/'+slug+'.jpg' , 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)       
    return path

@care_control
def users(request):

    User = get_user_model()
    writers_list = User.objects.all().filter(profile_activate=True)
    paginator = Paginator(writers_list, 5)

    page = request.GET.get('sayfa')
    try:
        writers = paginator.page(page)
    except PageNotAnInteger:
        writers = paginator.page(1)
    except EmptyPage:
        writers = paginator.page(paginator.num_pages)

    context={
        'writers_list':writers
    }
    return render(request, 'writers.html',context)