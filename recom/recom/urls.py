"""recom URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('recipe/recom/important/<user_id>/', views.recommend_from_retaining_ingredient),
    path('recipe/recom/expired/', views.recommend_from_urgent_expiration_date),
    path('admin/', admin.site.urls),
    path('node_to_django/', views.node_to_django),
    path('axios_from_node/', views.axios_from_node),
]
