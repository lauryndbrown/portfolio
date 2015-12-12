from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^home/', views.index, name='home'),
		url(r'^about/', views.about, name='about'),
		url(r'^portfolio/', views.projects, name='projects'),
		url(r'^blog/', views.blog, name='blog'),
		url(r'^contact/', views.contact, name='contact'),
]
