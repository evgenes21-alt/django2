from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
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
    template_name = "blog/blog_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "image", "content")
    success_url = reverse_lazy("blog:blog_list")

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "image", "content")
    success_url = reverse_lazy("blog:blog_list")

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")

