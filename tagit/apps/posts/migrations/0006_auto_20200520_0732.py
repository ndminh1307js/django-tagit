# Generated by Django 3.0.6 on 2020-05-20 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('created',)},
        ),
    ]
