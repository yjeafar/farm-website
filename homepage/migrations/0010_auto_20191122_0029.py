# Generated by Django 2.2.5 on 2019-11-22 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20191121_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmlocation',
            name='farmName',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
