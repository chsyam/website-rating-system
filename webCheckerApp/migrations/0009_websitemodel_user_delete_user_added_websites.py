# Generated by Django 4.1.2 on 2022-12-12 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webCheckerApp', '0008_rename_user_id_dislike_user_rename_user_id_like_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitemodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webCheckerApp.user'),
        ),
        migrations.DeleteModel(
            name='User_added_Websites',
        ),
    ]