# Generated by Django 3.1.1 on 2020-10-07 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0025_auto_20201007_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 7, 19, 27, 14, 294433)),
        ),
    ]