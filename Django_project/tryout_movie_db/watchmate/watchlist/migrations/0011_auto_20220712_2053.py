# Generated by Django 3.1.6 on 2022-07-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0010_auto_20220711_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]