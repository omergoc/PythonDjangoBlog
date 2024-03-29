
from django.db import models
from users.models import Account
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify


class Categories(models.Model):
    name=models.CharField(max_length=50,unique=True,verbose_name="Kategori Adı")
    description = models.TextField(blank=True, null=True, verbose_name="Kategori Açıklama")
    slug = models.SlugField(max_length=50,unique=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Kategoriler"


class Articles(models.Model):
    #id
    title = models.CharField(max_length=100,verbose_name="Başlık",unique=True)
    #view_count
    description = models.CharField(max_length=250,verbose_name="Açıklama", null=True)
    content = RichTextField(verbose_name="İçerik")
    #slug
    #image
    #category_name
    #category_slug
    #created_date
    #name
    #name_slug
    #views
    #types
    #available
    #category_id
    #last_edit_id
    #writer_id
    #kind


    writer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Yazar",
        blank=True,
        null=True,
        
    )
    last_edit = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Düzenleyen Editör",
        null=True,
        blank=True,
        related_name = "last_edit"
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Tarih")
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name="Kategori"
    )
    image = models.ImageField(upload_to = "static/upload/%Y/%m/%d", default="static/upload/default.jpg",  verbose_name="Resim(Önerilen:788x443)")
    slug = models.SlugField(max_length=200,unique=True,null=True, verbose_name="Seo Adres", editable=False)
    views = models.IntegerField(verbose_name="Görüntülenme Sayısı",default=0, editable=False)
    TYPE1 = "1"
    TYPE2 = "2"
    TYPE3 = '3'
    TYPE_LIST = [
        (TYPE1, 'Görsel Büyük Tasarımı'),
        (TYPE2, 'Dengeli Tasarımı'),
        (TYPE3, 'Text Ağırlıklı Tasarımı')
    ]
    types = models.CharField(
        max_length=2,
        choices=TYPE_LIST,
        default=TYPE3,
        verbose_name= "Tasarım Tipi"
    )
    available = models.BooleanField(default=False, verbose_name="Yayına Al")
    table_name = models.CharField(default="makale", editable=False,max_length=20)
    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Makaleler"
        #manages=False
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace('ı', 'i'))
        super(Articles, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    
class LikedArticle(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Kullanıcı",
        blank=True,
        null=True,
        
    )

    article = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE,
        verbose_name="İçerik",
        blank=True,
        null=True,
    )

class Images(models.Model):
    image_name = models.CharField(max_length=200,verbose_name="Resim Başlık")
    image_description=models.CharField(max_length=300,verbose_name="Resim Açıklama")
    image = models.ImageField(upload_to = "static/upload/%Y/%m/%d", default="static/upload/default.jpg", verbose_name="Resim")

    class Meta:
        verbose_name_plural = "Fotoğraflar"

    def __str__(self):
        return self.image_name

class News(models.Model):
    title = models.CharField(max_length=500,verbose_name="Başlık",unique=True)
    description = models.CharField(max_length=250,verbose_name="Açıklama", null=True)
    content = RichTextField(verbose_name="İçerik")
    writer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Yazar",
        blank=True,
        null=True,
        
    )
    last_edit_news = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Düzenleyen Editör",
        null=True,
        blank=True,
        related_name = "last_edit_news"
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Tarih")
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name="Kategori"
    )
    image = models.ImageField(upload_to = "static/upload/%Y/%m/%d", default="static/upload/default.jpg", verbose_name="Resim(Önerilen:788x443)")
    slug = models.SlugField(max_length=200,unique=True,null=True, verbose_name="Seo Adres", editable=False)
    views = models.IntegerField(verbose_name="Görüntülenme Sayısı",default=0, editable=False)
    TYPE1 = "1"
    TYPE2 = "2"
    TYPE3 = '3'
    TYPE_LIST = [
        (TYPE1, 'Görsel Büyük Tasarımı'),
        (TYPE2, 'Dengeli Tasarımı'),
        (TYPE3, 'Text Ağırlıklı Tasarımı')
    ]
    types = models.CharField(
        max_length=2,
        choices=TYPE_LIST,
        default=TYPE3,
        verbose_name= "Tasarım Tipi"
    )
    available = models.BooleanField(default=False, verbose_name="Yayına Al")
    table_name = models.CharField(default="haber", editable=False,max_length=20)

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Haberler"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace('ı', 'i'))
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Videos(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlık",unique=True)
    description = models.CharField(max_length=250,verbose_name="Açıklama", null=True)
    content = RichTextField(verbose_name="İçerik")
    video_link = models.CharField(max_length=250,verbose_name="Youtube Video Adresi", null=True)
    writer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Yazar",
        blank=True,
        null=True,
    )
    last_edit_video = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Düzenleyen Editör",
        null=True,
        blank=True,
        related_name = "last_edit_video"
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = "Tarih")
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name="Kategori"
    )
    image = models.ImageField(upload_to = "static/upload/%Y/%m/%d", default="static/upload/default.jpg", verbose_name="Resim(Önerilen:788x443)")
    slug = models.SlugField(max_length=200,unique=True,null=True, verbose_name="Seo Adres", editable=False)
    views = models.IntegerField(verbose_name="Görüntülenme Sayısı",default=0, editable=False)
    TYPE1 = "1"
    TYPE2 = "2"
    TYPE3 = '3'
    TYPE_LIST = [
        (TYPE1, 'Görsel Büyük Tasarımı'),
        (TYPE2, 'Dengeli Tasarımı'),
        (TYPE3, 'Text Ağırlıklı Tasarımı')
    ]
    types = models.CharField(
        max_length=2,
        choices=TYPE_LIST,
        default=TYPE3,
        verbose_name= "Tasarım Tipi"
    )
    table_name = models.CharField(default="video", editable=False,max_length=20)
    available = models.BooleanField(default=False, verbose_name="Yayına Al")

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Videolar"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace('ı', 'i'))
        super(Videos, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class LikedArticle(models.Model):
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Kullanıcı",
        blank=True,
        null=True,
    )
    post = models.IntegerField(blank=True, null=True)

    status = models.BooleanField(default=False, verbose_name="Durum", editable=False)


class Comments(models.Model):
    approver = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,blank=True,editable=False)
    article = models.ForeignKey(
        Articles,
        on_delete=models.CASCADE,
        verbose_name="Makale",
        null=True,
        editable=False
    )
    news = models.ForeignKey(
        News,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Haber",
        editable=False
    )
    videos = models.ForeignKey(
        Videos,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Video",
        editable=False
    )
    name = models.CharField(max_length=200,verbose_name="Ad Soyad")
    email = models.EmailField(verbose_name="E-Posta Adresi",blank=True)
    content = models.TextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True ,verbose_name="Tarih")
    available = models.BooleanField(default=False, verbose_name="Durum")

    class Meta:
        verbose_name_plural = "Yorumlar"

    def __str__(self):
        return self.name

class ReadPost(models.Model):
    read_id = models.CharField(max_length=1000, null=True)
    post = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
