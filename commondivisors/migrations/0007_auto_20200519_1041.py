# Generated by Django 3.0.6 on 2020-05-19 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondivisors', '0006_auto_20200519_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twonumbers',
            name='number1',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(3)]),
        ),
        migrations.AlterField(
            model_name='twonumbers',
            name='number2',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(3)]),
        ),
    ]
