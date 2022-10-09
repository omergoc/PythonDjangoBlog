from django import forms
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class LoginForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kullanıcı Adı'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Şifre'
    }))
    

class RegisterForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV3)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Kullanıcı Adı'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ad'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyad'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-Posta'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Şifre'
    }))
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tekrar Şifre'
    }))
    kvkk = forms.BooleanField()
    term_of_use = forms.BooleanField()

    def clean(self):
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        kvkk = self.cleaned_data.get('kvkk')
        term_of_use = self.cleaned_data.get('term_of_use')

        if  (' ' in username.strip()) == True :
            raise forms.ValidationError('Kullanıcı Adında Boşluk Olamaz.')
            
        if not kvkk and not term_of_use:
            raise forms.ValidationError('KVKK VE Kullanım Şartlarını Kabul Etmelisiniz !!!')
        elif password and confirm and password != confirm:
            raise forms.ValidationError('Şifreler Eşleşmiyor !!!')
        
        values = {
            "username" : username.strip(),
            "first_name" : first_name,
            "last_name" : last_name,
            "email" : email,
            "password" : password,
            "confirm" : confirm,
        }
        return values


class UpdateUserForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Ad'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyad'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'E-Posta'
    }))
    birthday = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Doğum Tarihi'
    }))
    about = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Hakkında'
    }))
    linkedin = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Linkedin'
    }))
    facebook = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Facebook'
    }))
    twitter = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Twitter'
    }))
    instagram = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'İnstagram'
    }))
    github = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Github'
    }))
    website = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Web Site'
    }))
    image  = forms.FileField()
    cv  = forms.FileField()


class PasswordChange(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder': 'Şifre'
    }))
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tekrar Şifre'
    }))

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')

        if password and confirm and password != confirm:
            print("hatalı sifreler")
            raise forms.ValidationError('Şifreler Eşleşmiyor !!!')
        
        values = {
            "password" : password,
            "confirm" : confirm,
        }
        return values