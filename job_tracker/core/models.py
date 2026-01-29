from django.db import models

# Create your models here.
class Application(models.Model):
    status_choices = [
        ("applied", "Applied"),
        ("interview", "Interview"),
        ("offer", "Offer"),
        ("rejected", "Rejected"),
    ]

    company_name = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    application_url = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=status_choices, blank=True)
    applied = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return (f"{self.job_title} at {self.company_name}")
    