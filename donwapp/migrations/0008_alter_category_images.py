# Generated by Django 4.2.6 on 2024-03-05 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donwapp', '0007_category_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='images',
            field=models.ImageField(upload_to='', verbose_name='category/'),
        ),
    ]