# Generated by Django 3.1.1 on 2020-10-07 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0024_auto_20201007_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 7, 19, 24, 42, 850668)),
        ),
    ]