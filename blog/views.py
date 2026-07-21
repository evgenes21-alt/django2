from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from blog.models import Blog


class BlogsDetailView(DetailView):
    model = Blog
    template_name = "blog/blogs_detail.html"
    context_object_name = "blog"  # переменная в шаблоне — blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Атомарно увеличиваем счётчик в БД (безопасно при нагрузках)
        Blog.objects.filter(pk=obj.pk).update(views_count=F('views_count') + 1)
        return obj


class BlogListView(ListView):
    model = Blog
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "image", "content")
    success_url = reverse_lazy("blog:post_list")