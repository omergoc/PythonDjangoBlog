# Generated by Django 3.2.6 on 2021-08-15 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='articles/images/default.jpg', upload_to='articles/images/%Y/%m/%d', verbose_name='Resim'),
        ),
    ]
