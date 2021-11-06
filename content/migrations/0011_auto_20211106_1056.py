# Generated by Django 3.2.9 on 2021-11-06 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_rename_meta_metaitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='metaitem',
            name='meta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='content.meta'),
        ),
    ]
