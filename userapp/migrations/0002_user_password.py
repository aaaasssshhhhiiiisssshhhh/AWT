# Generated by Django 4.0.5 on 2022-07-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]