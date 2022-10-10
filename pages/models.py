from tabnanny import verbose
from django.db import models
from users.models import Account

class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad Soyad",null=True)
    email = models.CharField(max_length=100,verbose_name="E-Posta",null=True)
    phone = models.CharField(max_length=100,verbose_name="Telefon",null=True)
    subject = models.CharField(max_length=100,verbose_name="Konu",null=True)
    content = models.TextField(verbose_name="Mesaj",null=True)

    created_date = models.DateTimeField(auto_now_add=True ,null=True, verbose_name = "Tarih")

    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=100,verbose_name="Başlık",null=True)
    url = models.CharField(max_length=100,verbose_name="Url",null=True)

    writer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Yazar",
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to = "static/upload/slider/%Y/%m/%d", default="static/upload/default.jpg", verbose_name="Resim(Önerilen:788x443)")

    created_date = models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return self.title