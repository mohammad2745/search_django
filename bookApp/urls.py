"""bookApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

# Import path module

from django.urls import path

# Import view

from book import views


# Define paths

urlpatterns = [

     path('admin/', admin.site.urls),

     path('', views.book_list, name='book_list'),

     path('/', views.book_detail, name='book_detail'),

     path('search/', views.search, name='search'),

]
