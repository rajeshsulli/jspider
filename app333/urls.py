from django.urls import path
from app333.views import *
app_name='anything'
urlpatterns=[
    path('rani/',rani,name='rani')
]