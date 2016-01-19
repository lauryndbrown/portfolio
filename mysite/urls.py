from django.conf.urls import url
from . import views


urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^index', views.index, name='home'),
		url(r'^about', views.about, name='about'),
		url(r'^projects', views.projects, name='projects'),
        url(r'^blog\/(?P<blog_post_id>[0-9]+)$', views.blog_post, name='blog_post'),
		url(r'^blog', views.blog, name='blog'),
		url(r'^contact', views.contact, name='contact'),
]
