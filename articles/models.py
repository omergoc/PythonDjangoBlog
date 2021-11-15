from django.db import models
from ckeditor.fields import RichTextField


class Categories(models.Model):
    name=models.CharField(max_length=50,unique=True,verbose_name="Kategori Adı")
    description = models.TextField(blank=True, null=True, verbose_name="Kategori Açıklama")
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name

class Articles(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlık",unique=True)
    description = models.CharField(max_length=250,verbose_name="Açıklama", null=True)
    content = RichTextField(verbose_name="İçerik")
    author = models.ForeignKey(
        'writers.Writers',
        on_delete=models.CASCADE,
        verbose_name="Yazar"
    )
    
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Categories,
        on_delete=models.DO_NOTHING,
        verbose_name="Kategori"
    )
    image = models.ImageField(upload_to = "static/upload/%Y/%m/%d", default="static/upload/default.jpg", verbose_name="Resim(Önerilen:788x443)")
    slug = models.SlugField(max_length=50,unique=True,null=True, verbose_name="Seo Adres")
    views = models.IntegerField(verbose_name="Görüntülenme Sayısı",default=0)
    available = models.BooleanField(default=True, verbose_name="Yayına Al")

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title
        

class Comments(models.Model):
    article = models.ForeignKey(
        Articles,
        on_delete=models.DO_NOTHING,
        verbose_name="Blog Başlık"
    )
    name = models.CharField(max_length=200,verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-Posta Adresi",blank=True)
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=False, verbose_name="Onayla")
    
    def __str__(self):
        return self.name


class Images(models.Model):
    image_name = models.CharField(max_length=200,verbose_name="Resim Başlık")
    image_description=models.CharField(max_length=300,verbose_name="Resim Açıklama")
    image = models.ImageField(upload_to = "static/upload/%Y/%m/%d", default="static/upload/default.jpg", verbose_name="Resim")

    
    def __str__(self):
        return self.image_name