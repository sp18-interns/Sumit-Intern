# Generated by Django 3.1.6 on 2022-07-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0009_alter_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_upcoming',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
