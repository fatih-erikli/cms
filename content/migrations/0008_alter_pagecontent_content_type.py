# Generated by Django 3.2.9 on 2021-11-05 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_pagecontent_external_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='content_type',
            field=models.IntegerField(choices=[(0, 'Header'), (1, 'Title'), (2, 'Paragraph'), (3, 'Image'), (4, 'List'), (5, 'Content'), (6, 'Navigation'), (7, 'Searchbar'), (8, 'Footer'), (9, 'Anchor')], default=0),
        ),
    ]
