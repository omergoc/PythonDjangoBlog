# Generated by Django 3.2.6 on 2022-09-11 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20220911_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='likedarticle',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.news', verbose_name='Haber'),
        ),
        migrations.AddField(
            model_name='likedarticle',
            name='status',
            field=models.BooleanField(default=False, editable=False, verbose_name='Durum'),
        ),
        migrations.AddField(
            model_name='likedarticle',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.videos', verbose_name='Video'),
        ),
        migrations.AlterField(
            model_name='likedarticle',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articles', verbose_name='Makale'),
        ),
    ]
