from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=255)
    address = models.TextField()

    def to_json(self):
        new_object = {}
        new_object['name'] = self.name
        new_object['decription'] = self.description
        new_object['city'] = self.city
        new_object['address'] = self.address
        return new_object
    
    def list_to_json(objects):
        return list(map(Company.to_json, objects))

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def to_json(self):
        new_object = {}
        new_object['name'] = self.name
        new_object['decription'] = self.description
        new_object['salary'] = self.salary
        new_object['company'] = self.company.to_json()
        return new_object
    
    def list_to_json(objects):
        return list(map(Vacancy.to_json, objects))

    def __str__(self):
        return self.name
