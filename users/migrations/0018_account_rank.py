# Generated by Django 3.2.6 on 2022-11-09 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_account_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='rank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.rank', verbose_name='Rütbe'),
        ),
    ]