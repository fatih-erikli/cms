# Generated by Django 3.2.9 on 2021-11-05 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('styles', '0003_alter_attribute_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='name',
            field=models.CharField(choices=[('margin', 'margin'), ('padding', 'padding'), ('font-family', 'font-family'), ('font-size', 'font-size'), ('border', 'border'), ('box-sizing', 'box-sizing'), ('background', 'background'), ('color', 'color'), ('width', 'width'), ('max-width', 'max-width'), ('height', 'height'), ('max-height', 'max-height')], max_length=255),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='style',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attributes', to='styles.style'),
        ),
        migrations.AlterField(
            model_name='style',
            name='extends',
            field=models.ManyToManyField(blank=True, related_name='_styles_style_extends_+', to='styles.Style'),
        ),
    ]
