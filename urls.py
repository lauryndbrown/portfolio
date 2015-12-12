from django.conf.urls import include url
from django.contrib import admin

urlpatterns = [
		url(r'^mysite/', include('mysite.urls')),
		url(r'^admin/', admin.site.urls),
]
