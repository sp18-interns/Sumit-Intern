# Generated by Django 4.0.6 on 2022-07-11 13:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(4), django.core.validators.MaxLengthValidator(4)]),
        ),
    ]
