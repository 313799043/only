# Generated by Django 2.0.3 on 2018-04-03 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courseorg_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='desc',
        ),
    ]
