# Generated by Django 3.2.9 on 2021-11-05 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_pagecontent_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent',
            name='html_tag',
            field=models.CharField(choices=[('div', 'div'), ('header', 'header'), ('aside', 'aside'), ('section', 'section'), ('footer', 'footer'), ('header', 'header'), ('p', 'paragraph'), ('h1', 'header-1'), ('h2', 'header-2'), ('h3', 'header-3'), ('h4', 'header-4'), ('h5', 'header-5')], default='div', max_length=255),
        ),
    ]
