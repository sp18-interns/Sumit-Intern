# Generated by Django 4.0.6 on 2022-07-11 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0008_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
