"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^track/studentsWithBooks/', include('track.urls')),
    url(r'^track/users/', include('track.urls')),
    url(r'^booksCheckedOut/(?P<param>[0-9]+)', include('track.urls')),
    url(r'^track/booksCheckedOut/(?P<param>[\w.-]+)/', include('track.urls')),
    url(r'^track/order/', include('track.urls')),
    url(r'^track/booksInSystemWithSearch/', include('track.urls')),
    url(r'^track/studentsInfo/', include('track.urls')),
    url(r'^track/application/', include('track.urls')),
    url(r'^track/', include('track.urls')),
    url(r'^admin/', admin.site.urls),
]
