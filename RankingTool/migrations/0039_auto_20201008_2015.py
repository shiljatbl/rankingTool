# Generated by Django 3.1.1 on 2020-10-08 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0038_auto_20201008_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordcrawl',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 20, 15, 55, 277967)),
        ),
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 20, 15, 55, 276975)),
        ),
    ]
