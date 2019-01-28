from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include(('health.urls', 'health'), namespace='health'))
]
