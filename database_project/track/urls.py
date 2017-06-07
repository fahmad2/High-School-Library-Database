from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^application', views.application),
 	url(r'^$', views.index),
	url(r'^studentsWithBooks', views.studentsWithBooks),
   	url(r'^users', views.users),
	url(r'^booksCheckedOut/(?P<param>[0-9]+)', views.booksCheckedOut),
	url(r'^booksCheckedOut/(?P<param>[\w.-]+)', views.booksCheckedOut),
	url(r'^order', views.orders),
	url(r'^booksInSystemWithSearch', views.booksInSystemWithSearch),
	url(r'^studentsInfo', views.studentsInfo),
]
