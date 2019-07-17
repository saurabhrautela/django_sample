from django.contrib import admin
from django.urls import path
# include is used to add URLs from the other apps in the root project
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^", include(("api.urls", "api"), namespace="api")),
    url(r"^", include(("profiles.urls", "profiles"), namespace="profiles")),
    url(r"^docs/", include_docs_urls(title="Django Sample")),
]
