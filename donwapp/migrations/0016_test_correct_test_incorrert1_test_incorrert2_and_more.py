# Generated by Django 4.2.6 on 2024-03-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donwapp', '0015_langcategory_test_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='correct',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='incorrert1',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='incorrert2',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='incorrert3',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
