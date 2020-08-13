from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Forecast(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    url = models.CharField(max_length=300, unique=True)
    summary = models.TextField()
    published = models.DateTimeField()
