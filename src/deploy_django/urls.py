from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello_world, name="home"),
    path("admin/", admin.site.urls),
    path("healthz/", views.healthz_view, name="healthz"),
]
