from django.urls import path
# from django.conf.urls import path
from django.urls import re_path as url
from django.contrib.auth import logout
from . import views

urlpatterns =[
	path('profile', views.profile, name= 'profile'),
	path('post',views.post, name = 'post'),
]
