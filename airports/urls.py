from rest_framework import routers
from .views import AirportsViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', AirportsViewSet, basename='airlines')

urlpatterns = router.urls