from django.db import models


class Book_info(models.Model):
    book_name = models.CharField(max_length=150, null=False)
    ISBN = models.CharField(max_length=150, null=False)
    author = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=700, null=True)
    price = models.IntegerField(null=True)
    edition = models.CharField(max_length=150, null=True)
    publisher = models.CharField(max_length=150, null=True)
    publishers = models.CharField(max_length=159, null=False)
