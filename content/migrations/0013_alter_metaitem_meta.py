# Generated by Django 3.2.9 on 2021-11-06 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_page_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metaitem',
            name='meta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='content.meta'),
        ),
    ]
