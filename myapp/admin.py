from .models import Industry, Job
from django.contrib import admin
from myapp.models import JobApplication

admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(JobApplication)