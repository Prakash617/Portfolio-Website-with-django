from ast import Index
from django import views
from django.urls import path
from .views import *
from app import views


app_name = "app"
urlpatterns = [
    path('', homeView.as_view(), name='index'),
    path('work/', workView.as_view(), name='work'),
    path('contact/', views.cform, name='contact'),
    path('ok/', okView.as_view(), name='ok'),
    path('ok/index.html',homeView.as_view(), name='in'),
]