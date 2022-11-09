from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser



class Rank(models.Model):
    title = models.CharField(max_length=200,null=True, default='Unvan Başlık',verbose_name="Unvan Başlık")
    description = models.CharField(max_length=500,null=True, default='Unvan Açıklama',verbose_name="Unvan Açıklama")

    class Meta:
        verbose_name_plural = "Kulanıcı Rütbeleri"

    def __str__(self):
        return self.title

class Account(AbstractUser):
    birthday = models.TextField(null=True, verbose_name="Doğum Tarihi")
    gender = models.CharField(
        max_length=6,
        null=True,
        verbose_name="Cinsiyet",
        choices=[('MALE','Erkek'),('FEMALE', 'Kadın')]
    )
    profile_activate =models.IntegerField(default=0,null=True, verbose_name="Portal Durum")
    description = models.TextField(verbose_name="Hakkında",null=True)
    cv = models.FileField(upload_to='static/upload/cv/%Y/%m/%d', null=True, default="static/upload/cv/default.pdf", verbose_name="CV Yükle")
    image = models.ImageField(upload_to = "static/upload/author/%Y/%m/%d", default="static/upload/author/default.jpg", null=True, verbose_name="Resim")
    facebook = models.CharField(max_length=500,null=True, default='/',verbose_name="facebook")
    linkedin = models.CharField(max_length=500,null=True,verbose_name="linkedin", default='/')
    slug = models.SlugField(max_length=50,unique=True,null=True, default='/',editable=False, verbose_name="Seo Adres")
    twitter = models.CharField(max_length=500, null=True,default='/',verbose_name="Twitter")
    instagram = models.CharField(max_length=500,null=True, default='/',verbose_name="İnstagram")
    youtube = models.CharField(max_length=500,null=True,default='/',verbose_name="Youtube")
    github = models.CharField(max_length=500,null=True, default='/',verbose_name="Github")
    website = models.CharField(max_length=500,null=True, default='/',verbose_name="Web Site")
    rank = models.ForeignKey(
        Rank,
        on_delete=models.CASCADE,
        verbose_name="Rütbe",
        null=True
    )

    class Meta:
        verbose_name_plural = "Kulanıcı Listesi"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username.replace('ı', 'i'))
        super(Account, self).save(*args, **kwargs)


class RankRequest(models.Model):
    username = models.CharField(max_length=200,verbose_name="Ad Soyad")
    title = models.CharField(max_length=200,null=True, default='Başlık',verbose_name="Başlık")
    description = models.CharField(max_length=500,null=True, default='Açıklama',verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Tarih")
    approver = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,blank=True,editable=False)
    available = models.BooleanField(default=False, verbose_name="Durum")

    class Meta:
        verbose_name_plural = "Kulanıcı Yetki Talepleri"

    def __str__(self):
        return self.title