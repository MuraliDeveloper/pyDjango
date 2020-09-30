# Generated by Django 2.2.6 on 2020-01-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.AddField(
            model_name='person',
            name='userType',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('user', 'USER')], default='admin', max_length=6),
        ),
    ]
