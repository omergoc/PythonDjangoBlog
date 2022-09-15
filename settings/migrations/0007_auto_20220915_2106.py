# Generated by Django 3.2.6 on 2022-09-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20220915_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='kvkk',
            field=models.FileField(default='static/upload/cv/default.pdf', null=True, upload_to='static/upload/kvkk/%Y/%m/%d', verbose_name='KVKK PDF'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='term_of_use',
            field=models.FileField(default='static/upload/cv/default.pdf', null=True, upload_to='static/upload/term_of_use/%Y/%m/%d', verbose_name='Term Of Use PDF'),
        ),
    ]
