# Generated by Django 2.1.3 on 2018-12-18 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProfileInfo',
            new_name='ProfileEntry',
        ),
    ]
