from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import auth
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

import random
from django.urls import reverse
from .models import Industry, Job
from .forms import JobForm, JobApplicationForm

def Aboutus(request):
    return render(request,'About us.html')
def Contactus(request):
        return render(request,'Contact us.html')

def home(request):
    return render(request, 'home.html')

def Footer(request):
    return render(request, 'footer.html')

def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            return redirect('job_detail', job_id=job.id)
    else:
        form = JobForm()
    return render(request, 'create_job.html', {'form': form})

class JobListByIndustryView(View):
    template_name = 'job_list_by_industry.html'

    def get(self, request, pk):
        industry = get_object_or_404(Industry, pk=pk)
        jobs = Job.objects.filter(industry=industry)
        return render(request, self.template_name, {'industry': industry, 'jobs': jobs})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Job, Industry, JobApplication
from django.core.exceptions import ValidationError


def apply_job(request, industry_id, job_id):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter')
        print(full_name)
        print(email)
        print(resume)
        job_application = JobApplication.objects.create(
            job_id=job_id,
            name=full_name,
            email=email,
            resume=resume,
            cover_letter=cover_letter,
        )
        job_application.save()
        # Optionally, you can add additional logic here, like sending a confirmation email to the applicant
        return redirect('myapp:success')  # Redirect to a success page after submission
    else:
        context = {
            'job': Job.objects.get(pk=job_id),
            'industry': Industry.objects.get(pk=industry_id),
        }
        return render(request, 'job_application_form.html', context)


def success(request):
    return render(request, 'success.html')

from django.shortcuts import render
from .models import Industry

def industry_list(request):
    industries = Industry.objects.all()
    return render(request, 'industry_list.html', {'industries': industries})

def send_otp(email, otp):
    subject = 'OTP Verification'
    message = f'Your OTP for registration is: {otp}'
    send_mail(subject, message, None, [email])



#def create_sector(request, industry_id):
#   industry = get_object_or_404(Industry, pk=industry_id)
#
#   if request.method == 'POST':
#      form = IndustryForm(request.POST)
#     if form.is_valid():
#        sector = form.save(commit=False)
#       sector.industry = industry
#      sector.save()
#     return redirect('industry_detail', pk=industry.id)

#else:
#   form = IndustryForm()

    #return render(request, 'create_sector.html', {'industry': industry, 'form': form})

from django.http import HttpResponseRedirect

# ...

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('myapp:register')

        otp_number = random.randint(1000, 9999)
        otp = str(otp_number)

        send_otp(email, otp)
        request.session['username'] = username
        request.session['email'] = email
        request.session['password'] = password
        request.session['otp'] = otp  # Add this line to store OTP in the session

        # Construct the URL using HttpResponseRedirect
        #return HttpResponseRedirect(f'/otp/{otp}/{username}/{password}/{email}/')
        # Alternatively, you can use reverse:
        return HttpResponseRedirect(reverse('myapp:otp', args=[otp, username, password, email]))

    else:
        return render(request, 'register.html')


def otp(request, otp, username, password, email):
    if request.method == "POST":
        uotp = request.POST['otp']
        otp_from_session = request.session.get('otp')

        if uotp == otp_from_session:
            username = request.session.get('username')
            email = request.session.get('email')
            password = request.session.get('password')

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('myapp:login')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')
            return redirect('myapp:otp', otp=otp, username=username, password=password, email=email)

    return render(request, 'otp.html',{'otp': otp, 'username': username, 'password': password, 'email': email})



def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('myapp:industry_list')
        else:
            messages.info(request,'Invalid user credentials')
            return redirect('myapp:login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout (request)
    return redirect('/')



