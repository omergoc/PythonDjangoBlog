# Generated by Django 3.2.6 on 2022-10-25 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20221010_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['-created_date'], 'verbose_name_plural': 'Makaleler'},
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Yorumlar'},
        ),
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name_plural': 'Fotoğraflar'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_date'], 'verbose_name_plural': 'Haberler'},
        ),
        migrations.AlterModelOptions(
            name='videos',
            options={'ordering': ['-created_date'], 'verbose_name_plural': 'Videolar'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(editable=False, max_length=500, null=True, unique=True, verbose_name='Seo Adres'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articles', verbose_name='Makale'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='available',
            field=models.BooleanField(default=False, verbose_name='Durum'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.news', verbose_name='Haber'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='videos',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.videos', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(editable=False, max_length=500, null=True, unique=True, verbose_name='Seo Adres'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=500, unique=True, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='slug',
            field=models.SlugField(editable=False, max_length=500, null=True, unique=True, verbose_name='Seo Adres'),
        ),
    ]
