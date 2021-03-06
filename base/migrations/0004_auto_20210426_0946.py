# Generated by Django 3.2 on 2021-04-26 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_posts_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.jpg', null=True, upload_to='images'),
        ),
    ]
