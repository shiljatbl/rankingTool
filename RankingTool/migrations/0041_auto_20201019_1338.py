# Generated by Django 3.1.1 on 2020-10-19 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0040_auto_20201019_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordcrawl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 19, 13, 38, 44, 476494)),
        ),
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 19, 13, 38, 44, 476494)),
        ),
    ]