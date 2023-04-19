from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    city = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"Company {self.name}"


class Vacancy(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return f"Vacancy {self.name} at {self.company}"