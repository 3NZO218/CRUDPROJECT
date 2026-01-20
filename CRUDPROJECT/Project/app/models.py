from django.db import models
from django.template.base import kwarg_re
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser




class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.IntegerField()
    pub_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    author = models.ManyToManyField(Author, blank=True)


    def __str__(self):
     return self.title



    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})

class Store(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book)

