# Generated by Django 3.2 on 2021-07-29 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0008_auto_20210729_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estimate',
            old_name='email_sent',
            new_name='is_sent',
        ),
    ]
