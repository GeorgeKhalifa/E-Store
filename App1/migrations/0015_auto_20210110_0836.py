# Generated by Django 3.1.4 on 2021-01-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0014_auto_20210110_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='discount_points',
        ),
        migrations.AddField(
            model_name='order',
            name='points',
            field=models.CharField(default=10, max_length=4),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='offer_points',
            field=models.PositiveIntegerField(blank=True, default=10),
        ),
    ]