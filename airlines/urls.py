from rest_framework import routers
from .views import AirlinesViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', AirlinesViewSet, basename='airlines')

urlpatterns = router.urls