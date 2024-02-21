from rest_framework import routers
from .views import AircraftViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', AircraftViewSet, basename='aircrafts')

urlpatterns = router.urls