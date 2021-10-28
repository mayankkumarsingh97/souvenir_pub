from django.urls import path
from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name="profile"),
     path('homepage', views.home, name="homepage"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('sendemail', views.sendemail, name="sendemail"),
    ]