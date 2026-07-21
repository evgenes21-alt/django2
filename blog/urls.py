from django.urls import path

from blog import views
from blog.views import BlogsDetailView, BlogListView, BlogUpdateView

app_name = "blog"

urlpatterns = [
    path("<int:pk>/",BlogsDetailView.as_view(), name="blogs_detail"),
    path("", BlogListView.as_view(), name="post_list"),
    path("blog/update", BlogUpdateView.as_view(), name="blog_update")
    ]