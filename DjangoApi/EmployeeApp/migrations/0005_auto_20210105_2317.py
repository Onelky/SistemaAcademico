# Generated by Django 3.1.4 on 2021-01-05 23:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0004_auto_20210105_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='createdDate',
            field=models.DateField(default=datetime.datetime(2021, 1, 5, 23, 17, 10, 910625)),
        ),
    ]
