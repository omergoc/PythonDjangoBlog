# Generated by Django 3.2.6 on 2022-11-09 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20221109_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='rank',
        ),
    ]
