# Generated by Django 3.2.6 on 2021-10-19 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_alter_order_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
    ]
