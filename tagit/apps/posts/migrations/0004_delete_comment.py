# Generated by Django 3.0.6 on 2020-05-19 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200519_1410'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
