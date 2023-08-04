"""problems20230404 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from measurements import views

urlpatterns = [
    # path('sensors/<int:id>/', views.ProjectAPIUpdate.as_view()),
    path('sensors/<str:name>/', views.ProjectAPIUpdate.as_view()),
    path('sensors/', views.ProjectAPICreate.as_view()),               # "К маршруту 'api/' добавили 'sensors/'."
    path('measurements/<int:pk>/', views.MeasurementView.as_view()),
    path('measurements/', views.MeasurementAPICreate.as_view()),
]
