# Generated by Django 2.2.5 on 2019-11-11 23:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20191111_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmowner',
            name='userId',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False),
        ),
    ]
