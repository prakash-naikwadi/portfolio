from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Login to Developer Prakash"
admin.site.site_title = "Welcome To Prakash's Dashbord"
admin.site.index_title = "Welcome To This Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
