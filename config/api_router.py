from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from anvara_assessment.record.api.views import RecordViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("records", RecordViewSet)


app_name = "api"
urlpatterns = router.urls
