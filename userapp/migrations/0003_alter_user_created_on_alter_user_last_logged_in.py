# Generated by Django 4.0.5 on 2022-07-22 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_logged_in',
            field=models.DateField(auto_now_add=True),
        ),
    ]