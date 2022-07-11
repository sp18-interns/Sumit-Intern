from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    year = models.IntegerField("Release Year", validators=[MinLengthValidator(4), MaxLengthValidator(6)])
    is_upcoming = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name, self.year
