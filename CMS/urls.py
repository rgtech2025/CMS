"""CMS URL Configuration

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
from django.urls import path
from Student import views as s
from Faculty import views as f


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',s.index,name='index'),
    path('std_register/',s.std_reg,name='std_register'),
    path('std_login',s.std_login,name='std_login'),
    path('std_home/',s.std_home,name='std_home'),
    path('about/',s.about,name='about'),
    path('contact/',s.contact,name='contact'),
    path('faculty_reg/',f.faculty_reg,name='faculty_reg'),
    path('faculty_login/',f.faculty_login,name='faculty_login'),
    path('faculty_home/',f.faculty_home,name='faculty_home'),
]
