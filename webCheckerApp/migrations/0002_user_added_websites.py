# Generated by Django 4.1.2 on 2022-12-11 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webCheckerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_added_Websites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webCheckerApp.user')),
                ('website_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webCheckerApp.websitemodel')),
            ],
        ),
    ]