# Generated by Django 3.1.1 on 2020-10-08 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0035_auto_20201008_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 20, 3, 1, 502293)),
        ),
    ]
