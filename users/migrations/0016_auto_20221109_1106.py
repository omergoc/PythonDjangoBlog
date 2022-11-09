# Generated by Django 3.2.6 on 2022-11-09 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20220916_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Unvan Başlık', max_length=200, null=True, verbose_name='Unvan Başlık')),
                ('description', models.CharField(default='Unvan Açıklama', max_length=500, null=True, verbose_name='Unvan Açıklama')),
            ],
            options={
                'verbose_name_plural': 'Kulanıcı Rütbeleri',
            },
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'Kulanıcı Listesi'},
        ),
        migrations.CreateModel(
            name='RankRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, verbose_name='Ad Soyad')),
                ('title', models.CharField(default='Başlık', max_length=200, null=True, verbose_name='Başlık')),
                ('description', models.CharField(default='Açıklama', max_length=500, null=True, verbose_name='Açıklama')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
                ('available', models.BooleanField(default=False, verbose_name='Durum')),
                ('approver', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.rank', verbose_name='Rütbe'),
        ),
    ]
