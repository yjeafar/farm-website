# Generated by Django 2.2.5 on 2019-11-11 23:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20191111_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmowner',
            name='password',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='farmowner',
            name='username',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
