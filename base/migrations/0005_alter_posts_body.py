# Generated by Django 3.2 on 2021-04-27 04:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210426_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]