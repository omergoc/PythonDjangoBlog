# Generated by Django 3.2.6 on 2022-09-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20220915_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]