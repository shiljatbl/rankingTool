# Generated by Django 3.1.1 on 2020-10-08 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0034_auto_20201008_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 8, 19, 42, 33, 240633)),
        ),
    ]