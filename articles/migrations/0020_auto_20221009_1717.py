# Generated by Django 3.2.6 on 2022-10-09 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20221008_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articles', verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='news',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.news', verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='videos',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.videos', verbose_name='Title'),
        ),
    ]
