# Generated by Django 2.1.2 on 2018-11-06 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='qty',
        ),
    ]
