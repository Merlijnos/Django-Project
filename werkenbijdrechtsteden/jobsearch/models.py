# jobsearch/models.py
from django.db import models

class JobListing(models.Model):
    job_title = models.CharField(max_length=200)
    employer_name = models.CharField(max_length=200)
    job_city = models.CharField(max_length=200)
    job_employment_type = models.CharField(max_length=200)
    job_educational_level = models.JSONField()  # Requires Django 3.1+
    job_min_salary = models.IntegerField()
    job_max_salary = models.IntegerField()
    job_posted_at_datetime_utc = models.DateTimeField()
    job_description = models.TextField()
    employer_website = models.URLField()

    def __str__(self):
        return self.job_title