# Generated by Django 3.1.4 on 2020-12-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_auto_20201206_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='null.png', upload_to='product_picture/'),
        ),
    ]
