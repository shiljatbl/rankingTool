# Generated by Django 3.1.1 on 2020-10-19 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0042_auto_20201019_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordcrawl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 19, 13, 46, 21, 766522)),
        ),
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 19, 13, 46, 21, 766522)),
        ),
    ]