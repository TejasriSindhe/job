from django.contrib.auth.models import User
from django.db import models
class Industry(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    Description=models.TextField()
    JobType = models.CharField(max_length=255)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    Companyname = models.CharField(max_length=200)
    salary = models.CharField(max_length=300)
    Location=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    def __str__(self):
        return f"Application for {self.job.title} by {self.name}"
