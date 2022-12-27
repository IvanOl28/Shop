from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# def category(request):
#     return render(request, 'category.html')
#
#
# def product_details(request):
#     return render(request, 'product-details.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')

