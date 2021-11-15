from django.shortcuts import render
from articles.models import Articles
from settings.models import Setting
from django.contrib import messages
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


@care_control
def index(request):
    articles = Articles.objects.order_by('-views')[:5]
    slider_article= Articles.objects.order_by('-id')[:2]
    context= {
        'articles':articles,
        'slider_article':slider_article
    }
    return render(request, 'index.html',context)

@care_control
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():       
            form.save()
            messages.success(request,"İşlem Başarılı...")
            return redirect(index)
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html',context)

    