from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', views.companies, name = 'home'),
    path('company/<int:pk>', views.company, name = 'company'),
    # path('company', views.company, name='company'),
    path('api/', views.api, name='api')

]
