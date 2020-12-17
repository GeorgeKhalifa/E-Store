# Generated by Django 3.1.4 on 2020-12-11 18:44

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.CharField(choices=[('s', 'small'), ('m', 'medium'), ('l', 'large')], default='', max_length=20),
        ),
    ]
