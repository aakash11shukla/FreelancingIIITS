# Generated by Django 2.1.1 on 2018-10-19 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0004_auto_20181019_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='time_of_application',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 6, 13, 3, 908400)),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='time_of_selection',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 6, 13, 3, 908820)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recieving_time',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 6, 13, 3, 910670)),
        ),
        migrations.AlterField(
            model_name='project',
            name='postedOn',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 6, 13, 3, 906510)),
        ),
        migrations.AlterField(
            model_name='task',
            name='addedOn',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 19, 6, 13, 3, 906984)),
        ),
    ]
