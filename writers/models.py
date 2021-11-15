from django.db import models

class Writers(models.Model):
    author = models.CharField(verbose_name="Ad Soyad", max_length=200)
    description = models.TextField(verbose_name="Hakkında")
    image = models.ImageField(upload_to = "static/upload/author/%Y/%m/%d", default="static/upload/author/default.jpg", verbose_name="Resim")
    slug = models.SlugField(max_length=50,unique=True,null=True, verbose_name="Seo Adres")
    facebook = models.CharField(max_length=500,verbose_name="facebook")
    twitter = models.CharField(max_length=500,verbose_name="Twitter")
    instagram = models.CharField(max_length=500,verbose_name="İnstagram")
    youtube = models.CharField(max_length=500,verbose_name="Youtube")
    github = models.CharField(max_length=500,verbose_name="Github")
    website = models.CharField(max_length=500,verbose_name="Web Site")

    def __str__(self):
        return self.author