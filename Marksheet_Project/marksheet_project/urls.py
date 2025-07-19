from django.contrib import admin
from django.urls import path
from marksheet_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('submit/', views.submit_marksheet, name='submit_marksheet'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
]
