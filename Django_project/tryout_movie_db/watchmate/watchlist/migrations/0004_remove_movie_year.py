# Generated by Django 4.0.6 on 2022-07-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0003_alter_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
