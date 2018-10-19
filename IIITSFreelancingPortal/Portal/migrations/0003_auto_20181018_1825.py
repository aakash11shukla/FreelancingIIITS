# Generated by Django 2.1.1 on 2018-10-18 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portal', '0002_auto_20181018_1823'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='hasRead',
            new_name='has_read',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='receivingTime',
        ),
        migrations.AddField(
            model_name='notification',
            name='recieving_time',
            field=models.DateTimeField(blank=True, default=None),
        ),
        migrations.AddField(
            model_name='notification',
            name='sending_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 18, 25, 27, 851550)),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='time_of_application',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 18, 25, 27, 849300)),
        ),
        migrations.AlterField(
            model_name='contributor',
            name='time_of_selection',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 18, 25, 27, 849720)),
        ),
        migrations.AlterField(
            model_name='project',
            name='postedOn',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 18, 25, 27, 847402)),
        ),
        migrations.AlterField(
            model_name='task',
            name='addedOn',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 18, 25, 27, 847876)),
        ),
    ]
