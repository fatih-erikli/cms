# Generated by Django 3.2.9 on 2021-11-05 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_rename_name_unidecoded_page_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontent',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='content.page'),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content', to='content.pagecontent'),
        ),
    ]
