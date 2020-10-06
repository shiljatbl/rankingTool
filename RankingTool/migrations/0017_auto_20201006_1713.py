# Generated by Django 3.1.1 on 2020-10-06 15:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0016_auto_20201006_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='keyword',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RankingTool.keyword'),
        ),
        migrations.AlterField(
            model_name='scrapeproduct',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 17, 13, 31, 757552)),
        ),
    ]
