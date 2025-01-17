# Generated by Django 4.2.14 on 2025-01-13 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profilemodel_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='product_image',
            field=models.ImageField(default=1, upload_to='product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='profile_image',
            field=models.ImageField(default=1, upload_to='profile'),
            preserve_default=False,
        ),
    ]
