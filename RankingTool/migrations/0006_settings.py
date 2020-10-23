# Generated by Django 3.1.1 on 2020-10-23 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RankingTool', '0005_auto_20201022_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=15)),
                ('no_of_pages', models.IntegerField(default=3)),
            ],
        ),
    ]