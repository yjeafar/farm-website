# Generated by Django 2.2.5 on 2019-12-04 23:46

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0019_auto_20191130_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='thumb',
            field=sorl.thumbnail.fields.ImageField(default='media/media/no-image-available.jpg', upload_to='media/'),
        ),
    ]
