# Generated by Django 4.0.3 on 2022-04-11 11:34

import authentication.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_user_id'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', authentication.models.UserManager()),
            ],
        ),
    ]
