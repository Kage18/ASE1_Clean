# Generated by Django 2.1.2 on 2018-11-04 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0013_vendorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 4, 18, 37, 47, 679944)),
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 4, 18, 37, 47, 679944)),
        ),
    ]
