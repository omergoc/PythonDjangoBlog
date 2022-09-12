# Generated by Django 3.2.6 on 2022-09-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_account_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='facebook',
            field=models.CharField(default='/', max_length=500, null=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='account',
            name='github',
            field=models.CharField(default='/', max_length=500, null=True, verbose_name='Github'),
        ),
        migrations.AlterField(
            model_name='account',
            name='instagram',
            field=models.CharField(default='/', max_length=500, null=True, verbose_name='İnstagram'),
        ),
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.SlugField(default='/', editable=False, null=True, unique=True, verbose_name='Seo Adres'),
        ),
        migrations.AlterField(
            model_name='account',
            name='twitter',
            field=models.CharField(default='/', max_length=500, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='account',
            name='website',
            field=models.CharField(default='/', max_length=500, null=True, verbose_name='Web Site'),
        ),
        migrations.AlterField(
            model_name='account',
            name='youtube',
            field=models.CharField(default='/', max_length=500, null=True, verbose_name='Youtube'),
        ),
    ]
