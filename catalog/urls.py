from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import SplitSystemListView, SplitDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path("", SplitSystemListView.as_view(), name="split_system"),
    path("catalog/<int:pk>/", SplitDetailView.as_view(), name="split_detail"),
]
