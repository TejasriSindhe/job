from .models import Job
from django import forms
class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'resume', 'cover_letter']

# forms.py

from django import forms
from .models import Industry

class IndustryForm(forms.ModelForm):
    class Meta:
        model = Industry
        fields = ['name']  # Add other fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add any additional customization for your form fields here
