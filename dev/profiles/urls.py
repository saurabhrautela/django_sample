from rest_framework.routers import DefaultRouter
from django.urls import path, include
from profiles import views

router = DefaultRouter()
# We do not need to add the `base_name` as we have defined `queryset` in the viewset
# so it can be determined using the model
router.register("profiles_viewset", views.UserProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]
