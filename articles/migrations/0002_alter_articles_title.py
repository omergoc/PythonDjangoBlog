# Generated by Django 3.2.6 on 2021-08-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Başlık'),
        ),
    ]
