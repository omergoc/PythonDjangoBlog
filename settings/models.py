from django.db import models

# Create your models here.

class Setting(models.Model):
    Logo = models.ImageField(upload_to = "static/upload/site/%Y/%m/%d", default="static/upload/site/default.png", verbose_name="Logo")
    title = models.CharField(max_length=50, verbose_name="Başlık",default="Siberatay")
    author= models.CharField(max_length=200, verbose_name="Yazar",default="Siberatay")
    kvkk = models.FileField(upload_to='static/upload/kvkk/%Y/%m/%d', default="static/upload/cv/default.pdf", null=True, verbose_name="KVKK PDF")
    term_of_use = models.FileField(upload_to='static/upload/term_of_use/%Y/%m/%d',default="static/upload/cv/default.pdf", null=True, verbose_name="Term Of Use PDF")
    descripton= models.TextField(max_length=500, verbose_name="Açıklama",default="blog content")
    footer = models.CharField(max_length=150, verbose_name="Site Alt Açıklama")
    facebook = models.CharField(max_length=500,verbose_name="facebook")
    twitter = models.CharField(max_length=500,verbose_name="Twitter")
    instagram = models.CharField(max_length=500,verbose_name="İnstagram")
    youtube = models.CharField(max_length=500,verbose_name="Youtube")
    image1 = models.ImageField(upload_to = "static/upload/site/%Y/%m/%d", default="static/upload/site/reklam1.jpg", verbose_name="Resim(Önerilen:300x600)")
    image1Url = models.CharField(max_length=500,verbose_name="Reklam 1 Url Adres")
    image2 = models.ImageField(upload_to = "static/upload/site/%Y/%m/%d", default="static/upload/site/reklam1.jpg", verbose_name="Resim(Önerilen:728x90)")
    image2Url = models.CharField(max_length=500,verbose_name="Reklam 2 Url Adres")
    image3 = models.ImageField(upload_to = "static/upload/site/%Y/%m/%d", default="static/upload/site/reklam2.jpg", verbose_name="Resim(Önerilen:728x90)")
    image3Url = models.CharField(max_length=500,verbose_name="Reklam 3 Url Adres")    
    available = models.BooleanField(default=False, verbose_name="Bakım Durum")

    def __str__(self):
        return "Site Ayarları"
    
    class Meta:
        verbose_name_plural = "Ayar Listesi"