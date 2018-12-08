# Generated by Django 2.1.3 on 2018-12-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_auto_20181208_1928'),
        ('cart', '0003_auto_20181208_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='vendor',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor',
            field=models.ManyToManyField(to='vendor.VendorProfile'),
        ),
    ]
