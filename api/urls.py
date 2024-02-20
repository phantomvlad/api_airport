from django.contrib import admin
from django.urls import path
from rest_framework import routers
from aircrafts.views import AircraftViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'aircrafts', AircraftViewSet, basename='aircrafts')

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
