# Generated by Django 3.2.6 on 2021-10-19 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
