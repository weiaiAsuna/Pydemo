"""pydemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from second_app import views

urlpatterns = [
    # url(r'^$',views.login),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^json/', views.json),
    url(r'^getjson/', views.getjson),
    url(r'^list-(?P<page>\d+)/', views.list),
    url(r'^list_down-(?P<nid>\d+)/', views.download_file),
    url(r'^user_del-(?P<nid>\d+)/', views.user_del),
    url(r'^user_edit-(?P<uid>\d+)/', views.user_edit),
]
