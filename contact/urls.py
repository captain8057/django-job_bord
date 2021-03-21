from . import views
from django.contrib import admin
from django.urls import path ,include



app_name='contact   '

urlpatterns = [
    path('',views.send_meseage ,name='contact'),

]
