from django.contrib import admin
from django.urls import path
from . import views

from .views import contact_view
app_name = 'ask_me'

urlpatterns = [
    path('contact_view/', views.contact_view, name='contact_view'),
]