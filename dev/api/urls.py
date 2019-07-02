from django.conf.urls import url
from rest_framework import routers
from api.views import (
    vista_de_el_hola_mundo,
    NamasteVishwaKaDrishya,
    HelloWorldView,
    PersonView,
)

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += {
    url(r"^hola", vista_de_el_hola_mundo, name="hola_mundo"),
    url(r"^namaste", NamasteVishwaKaDrishya.as_view(), name="namaste_vishwa"),
    url(r"^hello", HelloWorldView.as_view(), name="hello_world"),
    url(r"^person", PersonView.as_view(), name="person"),
}
