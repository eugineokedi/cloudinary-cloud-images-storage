# Generated by Django 5.1.4 on 2024-12-19 16:24

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
    ]