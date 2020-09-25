from . import views
from django.contrib import admin
from django.urls import path ,include





urlpatterns = [
    path('',views.job_list),
    path('<int:id>',views.job_detail),
]
