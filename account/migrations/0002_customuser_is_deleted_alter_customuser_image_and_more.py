# Generated by Django 4.2 on 2023-09-22 06:58

import account.services
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=account.services.get_path_upload_avatar, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg']), account.services.validate_size_image]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='\n        Telefon raqam: 13 ta belgidan iborat bolishi kerak. P.s: +998912345678\n    ', regex='^[+]998\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='overview',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
