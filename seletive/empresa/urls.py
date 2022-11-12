from django.urls import path
from . import views

urlpatterns = [
    path('nova_empresa/', views.nova_empresa, name='nova_empresa'),
    
]