# Generated by Django 4.1.2 on 2022-12-12 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webCheckerApp', '0006_remove_user_added_website_website_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_added_Website',
        ),
    ]
