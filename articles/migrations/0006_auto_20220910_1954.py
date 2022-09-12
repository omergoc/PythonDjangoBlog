# Generated by Django 3.2.6 on 2022-09-10 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_comments_approver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.types', verbose_name='Tür'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.categories', verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles', verbose_name='Blog Başlık'),
        ),
    ]
