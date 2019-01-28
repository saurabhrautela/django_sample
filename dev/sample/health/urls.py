from django.conf.urls import url
from rest_framework import routers
from health.views import HealthView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += {
    url(r'^health/', HealthView.as_view(), name='health_check')
}