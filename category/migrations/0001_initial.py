# Generated by Django 3.2.6 on 2021-10-19 06:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('cat_name', models.CharField(max_length=200)),
                ('cat_description', models.TextField(blank=True, null=True)),
                ('cat_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('packaging_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_charge', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cat_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
