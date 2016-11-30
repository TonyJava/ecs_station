"""ecs_ground_station URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from station_serial.views import * ;

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^station/list_command?.*$', list_command),
    url(r'^station/insert_command?.*$', insert_command),
    url(r'^station/delete_command?.*$', delete_command),
    url(r'^station/list_command?.*$', list_var),
    url(r'^station/insert_command?.*$', insert_var),
    url(r'^station/delete_command?.*$', delete_var),
]
