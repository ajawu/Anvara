from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from anvara_assessment.record.api.views import RecordViewSet
from anvara_assessment.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("records", RecordViewSet)


app_name = "api"
urlpatterns = router.urls
