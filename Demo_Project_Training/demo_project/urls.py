"""
URL configuration for demo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from demo_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home_page, name= 'HomePage'),
    path('aboutUs/', views.aboutUs, name= "About"),
    path('user_form/', views.user_form),
    path('contact/', views.contact),
    path('services/', views.services),
    path('help_page/', views.help_page),
    path('blog/', views.blog),
    path('submitform/',views.submitform, name= 'submitform'),
]   


"""
    # Dynamic URL 
    path('name/<str:amin>/', views.Dynamicdata),       
    path('user/<int:id>/', views.user_detail),          
    path('blog/<slug:slug>/', views.blog_detail), 
"""  


"""
path('about/', views.about),
path('serviecs/', views.services),
path('contact/', views.contact),
path('blog/', views.blog),
path('help/', views.help),
"""


"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
]
"""