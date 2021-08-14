from django.shortcuts import render


def products(request):
    context = {}
    return render(request, "products.html", context)

