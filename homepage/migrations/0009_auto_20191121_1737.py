# Generated by Django 2.2.5 on 2019-11-21 22:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_auto_20191121_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmlocation',
            name='farmNumber',
        ),
        migrations.AddField(
            model_name='farmlocation',
            name='farmName',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
