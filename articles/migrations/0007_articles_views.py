# Generated by Django 3.2.6 on 2021-08-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articles_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Görüntülenme Sayısı'),
        ),
    ]
