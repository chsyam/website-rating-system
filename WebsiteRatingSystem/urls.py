"""WebChecker URL Configuration

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
from django.urls import path, include
from WRSapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('dictionary_api/', views.dictionary_api),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/add/', views.add_New_Website, name="add"),
    path('dashboard/check/', views.check, name="check"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('dashboard/logout/', views.logout, name="logout"),
]
