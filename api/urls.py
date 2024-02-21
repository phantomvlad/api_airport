from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('aircrafts', include('aircrafts.urls')),
	path('airlines', include('airlines.urls')),
	path('airports', include('airports.urls')),
]


