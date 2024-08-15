# jobs/models.py
from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    application_date = models.DateField()
    status = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    portfolio = models.FileField(upload_to='portfolios/', blank=True, null=True)

    def __str__(self):
        return self.title
