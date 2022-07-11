from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator, DecimalValidator


class Movie(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
