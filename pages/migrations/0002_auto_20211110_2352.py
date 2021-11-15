# Generated by Django 3.2.6 on 2021-11-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='content',
            field=models.TextField(null=True, verbose_name='Mesaj'),
        ),
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name='E-Posta'),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='Ad Soyad'),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=100, null=True, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=100, null=True, verbose_name='Konu'),
        ),
    ]
