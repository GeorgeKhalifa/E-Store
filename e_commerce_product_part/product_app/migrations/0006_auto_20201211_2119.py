# Generated by Django 3.1.4 on 2020-12-11 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_auto_20201211_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, upload_to='product_pictures'),
        ),
    ]
