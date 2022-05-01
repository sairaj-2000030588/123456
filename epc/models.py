from django.db import models

# Create your models here.
DEPARTMENT_CHOICES = {
    ("CSE", 'cse'),
    ("CSIT", 'csit'),
    ("AIDS", 'aids'),
}


class Employee(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
