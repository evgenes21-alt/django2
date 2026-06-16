from django.urls import path
from . import views
from .apps import CatalogConfig
from catalog.views import split_system,split_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", split_system, name="split_system"),
    path("<int:pk>/",split_detail, name="split_detail"),
]
