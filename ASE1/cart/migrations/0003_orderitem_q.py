# Generated by Django 2.1.2 on 2018-11-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_remove_orderitem_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='q',
            field=models.IntegerField(null=True),
        ),
    ]
