"""core URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from card_interactions import views


urlpatterns = [
    path('<int:id>/open', views.get_card_details, name='get_card_info'),
    path('<int:id>/create/' ,views.create_card, name='Create Card'),
    path('<int:id>/edit/title/', views.edit_card_title, name='Edit Card'),
    path('<int:id>/edit/description/', views.edit_card_description, name='Edit Card'),
    path('<int:id>/like/', views.register_like, name='Register like'),
    path('<int:id>/delete/', views.delete_card, name='Delete card'),
]
