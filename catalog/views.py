from msilib.schema import ListView

from django.http import HttpResponse

from django.shortcuts import render, get_list_or_404, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView


class SplitSystemListView(ListView):
    model = Product


class SplitDetailView(DetailView):
    model = Product

#
# def split_detail(request,pk):
#     split = get_object_or_404(Product ,pk=pk)
#     context = {"split": split}
#     return render(request, "product_detail.html", context)
#
