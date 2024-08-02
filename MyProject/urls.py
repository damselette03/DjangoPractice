"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

# from schema import *
from restaurants.views import menu , home , search

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('accounts/', include('allauth.urls')),
    path('menu/', menu, name='menu'),
    path('' , home , name='home'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('accounts/', include('restaurants.urls')),  # 包含应用程式的urls
    path('search/', search , name='search'),
]
