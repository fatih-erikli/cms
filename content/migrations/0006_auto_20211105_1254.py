# Generated by Django 3.2.9 on 2021-11-05 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_pagecontent_html_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecontent',
            name='external_url',
            field=models.CharField(default=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pagecontent',
            name='linked_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='links', to='content.page'),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='content_type',
            field=models.IntegerField(choices=[(0, 'Header'), (1, 'Title'), (2, 'Paragraph'), (3, 'Image'), (4, 'List'), (5, 'Content'), (6, 'Navigation'), (7, 'Searchbar'), (8, 'Footer')], default=0),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='html_tag',
            field=models.CharField(choices=[('div', 'div'), ('header', 'header'), ('aside', 'aside'), ('section', 'section'), ('footer', 'footer'), ('header', 'header'), ('p', 'paragraph'), ('h1', 'header-1'), ('h2', 'header-2'), ('h3', 'header-3'), ('h4', 'header-4'), ('h5', 'header-5'), ('a', 'anchor'), ('time', 'Datetime')], default='div', max_length=255),
        ),
    ]