# Generated by Django 3.0.6 on 2020-05-19 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondivisors', '0005_auto_20200519_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twonumbers',
            name='number2',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
