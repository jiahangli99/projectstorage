from django.db import models
from django.urls import reverse

# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('status_detail', kwargs={'pk': self.id})


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    status = models.ManyToManyField(Status)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('about')

class Date(models.Model):
    date = models.DateField('Worked Date')

    #Create a cat_id FK
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']