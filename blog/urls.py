from django.urls import path

from blog import views
from blog.views import BlogsDetailView, BlogListView, BlogUpdateView, BlogCreateView, BlogDeleteView

app_name = "blog"

urlpatterns = [
    path("<int:pk>/",BlogsDetailView.as_view(), name="blogs_detail"),
    path("", BlogListView.as_view(), name="blog_list"),
    path("create/", BlogCreateView.as_view(), name="blog_create"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete")
    ]