# Generated by Django 3.2.6 on 2021-08-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20210821_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='articles/images/default.jpg', upload_to='articles/images/%Y/%m/%d', verbose_name='Resim(Önerilen:788x443)'),
        ),
    ]
