# Generated by Django 3.2 on 2021-04-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_posts_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.jpeg', null=True, upload_to='images'),
        ),
    ]
