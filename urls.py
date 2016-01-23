from django.conf.urls import include url
from django.contrib import admin

urlpatterns = [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}, name="media"),
	#	url(r'^mysite/', include('mysite.urls')),
		url(r'^admin/', admin.site.urls),
]
