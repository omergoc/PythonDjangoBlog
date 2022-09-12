# Generated by Django 3.2.6 on 2022-09-09 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220909_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.TextField(null=True, verbose_name='Hakkında'),
        ),
        migrations.AlterField(
            model_name='account',
            name='facebook',
            field=models.CharField(max_length=500, null=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Erkek'), ('FEMALE', 'Kadın')], max_length=6, null=True, verbose_name='Cinsiyet'),
        ),
        migrations.AlterField(
            model_name='account',
            name='github',
            field=models.CharField(max_length=500, null=True, verbose_name='Github'),
        ),
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(default='static/upload/author/default.jpg', null=True, upload_to='static/upload/author/%Y/%m/%d', verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='account',
            name='instagram',
            field=models.CharField(max_length=500, null=True, verbose_name='İnstagram'),
        ),
        migrations.AlterField(
            model_name='account',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True, verbose_name='Seo Adres'),
        ),
        migrations.AlterField(
            model_name='account',
            name='twitter',
            field=models.CharField(max_length=500, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='account',
            name='website',
            field=models.CharField(max_length=500, null=True, verbose_name='Web Site'),
        ),
        migrations.AlterField(
            model_name='account',
            name='youtube',
            field=models.CharField(max_length=500, null=True, verbose_name='Youtube'),
        ),
    ]
