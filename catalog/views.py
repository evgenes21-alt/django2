from django.http import HttpResponse

from django.shortcuts import render, get_list_or_404, get_object_or_404
from catalog.models import Product


def split_system(request):
    catalog = Product.objects.all()
    context = {"catalog": catalog}
    return render(request, "split_list.html", context)


def split_detail(request,pk):
    split = get_object_or_404(Product ,pk=pk)
    context = {"split": split}
    return render(request, "split_detail.html", context)

