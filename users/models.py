from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    birthday = models.DateTimeField(null=True)
    gender = models.CharField(
        max_length=6,
        null=True,
        verbose_name="Cinsiyet",
        choices=[('MALE','Erkek'),('FEMALE', 'Kadın')]
    )
    description = models.TextField(verbose_name="Hakkında",null=True)
    image = models.ImageField(upload_to = "static/upload/author/%Y/%m/%d", default="static/upload/author/default.jpg", null=True, verbose_name="Resim")
    facebook = models.CharField(max_length=500,null=True, default='/',verbose_name="facebook")
    linkedin = models.CharField(max_length=500,null=True,verbose_name="linkedin")
    slug = models.SlugField(max_length=50,unique=True,null=True, default='/',editable=False, verbose_name="Seo Adres")
    twitter = models.CharField(max_length=500, null=True,default='/',verbose_name="Twitter")
    instagram = models.CharField(max_length=500,null=True, default='/',verbose_name="İnstagram")
    youtube = models.CharField(max_length=500,null=True,default='/',verbose_name="Youtube")
    github = models.CharField(max_length=500,null=True, default='/',verbose_name="Github")
    website = models.CharField(max_length=500,null=True, default='/',verbose_name="Web Site")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username.replace('ı', 'i'))
        super(Account, self).save(*args, **kwargs)

