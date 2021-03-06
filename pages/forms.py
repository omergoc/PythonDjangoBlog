from django import forms
from django.forms.widgets import TextInput
from . models import Contact

class ContactForm(forms.ModelForm):
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
        'placeholder':'Konu'
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Mesaj'
    }))

    class Meta:
        model = Contact
        fields = ['name','email','phone','subject','content']