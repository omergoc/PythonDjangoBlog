from django import forms
from . models import Contact
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ad Soyad'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-Posta'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Telefon'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Konu'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Mesaj'
    }))

    class Meta:
        model = Contact
        fields = ['captcha','name','email','phone','subject','content']

