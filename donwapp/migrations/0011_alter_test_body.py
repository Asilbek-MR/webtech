# Generated by Django 4.2.6 on 2024-03-06 04:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donwapp', '0010_rename_images_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
