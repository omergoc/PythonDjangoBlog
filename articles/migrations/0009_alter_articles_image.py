# Generated by Django 3.2.6 on 2021-08-21 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_comments_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='articles/slider/default.png', upload_to='articles/slider/%Y/%m/%d', verbose_name='Slider(Önerilen:788x443)'),
        ),
    ]
