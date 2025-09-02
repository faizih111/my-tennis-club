from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("members.urls")),  # This routes root URL to the members app
    path("admin/", admin.site.urls),  # This keeps the admin panel working
]
