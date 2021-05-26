from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login/', views.login, name="about"),
    path('register', views.register, name="register"),
    # path('details', views.details, name="details"),
    path('electronics', views.electronics, name="electronics"),
    path('employees', views.employees, name="employees"),
    # path('register/details', views.details, name="details"),
    path('update', views.update, name="update"),
    path('delete', views.delete, name="delete"),
    
]