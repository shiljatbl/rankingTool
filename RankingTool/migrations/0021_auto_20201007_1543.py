# Generated by Django 3.1.1 on 2020-10-07 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0020_auto_20201007_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 7, 15, 43, 48, 637476)),
        ),
        migrations.AlterField(
            model_name='scrapeproduct',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]