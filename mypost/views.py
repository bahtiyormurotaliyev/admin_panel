from django.shortcuts import render

def dynamic_page(request):
    return render(request, 'main.html')

def post_page(request):
    return render(request, 'myapp/post_page.html')

def content_page(request):
    return render(request, 'myapp/content_page.html')

def detail_page(request):
    return render(request, 'myapp/detail_page.html')

