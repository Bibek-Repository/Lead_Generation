from django.urls import path
from . import views

urlpatterns = [
    path('', views.capture_lead, name='lead_form'),
    path('success/', views.success, name='success'),
]