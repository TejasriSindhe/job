from django.urls import path
from myapp.views import home,create_job,JobListByIndustryView,apply_job,success,industry_list,otp,login,logout,register,Aboutus,Contactus,Footer
app_name="myapp"
urlpatterns=[
    path('',home,name='home'),
    path('jobs/create/', create_job, name='create_job'),
    path('industry/<int:pk>/jobs/', JobListByIndustryView.as_view(), name='job_list_by_industry'),
    path('apply_job/<int:industry_id>/<int:job_id>/', apply_job, name='apply_job'),
    path('success/',success,name='success'),
    path('industries/', industry_list, name='industry_list'),
    path('otp/<str:otp>/<str:username>/<str:password>/<str:email>/',otp, name='otp'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('register/',register,name='register'),
    path('About /',Aboutus,name='About us'),
    path('Contact /',Contactus,name='Contact us'),
    path('Footer /',Footer,name='footer'),
]
