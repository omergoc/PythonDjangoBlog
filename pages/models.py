from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad Soyad",null=True)
    email = models.CharField(max_length=100,verbose_name="E-Posta",null=True)
    phone = models.CharField(max_length=100,verbose_name="Telefon",null=True)
    subject = models.CharField(max_length=100,verbose_name="Konu",null=True)
    content = models.TextField(verbose_name="Mesaj",null=True)

    created_date = models.DateTimeField(auto_now_add=True ,null=True)

    def __str__(self):
        return self.name