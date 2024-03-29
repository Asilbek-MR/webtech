# Generated by Django 4.2.6 on 2024-03-02 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donwapp', '0002_rename_test_feedback_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=255)),
                ('read_time', models.IntegerField(default=0)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('number', models.IntegerField(default=0)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incorrert1', models.CharField(max_length=255)),
                ('incorrert2', models.CharField(max_length=255)),
                ('incorrert3', models.CharField(max_length=255)),
                ('correct', models.CharField(max_length=255)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donwapp.test')),
            ],
        ),
    ]
