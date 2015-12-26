from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context = []
    return render(request, 'index.html', context)

def about(request):
    context = []
    return render(request, 'about.html', context)

def projects(request):
    context = []
    return render(request, 'projects.html', context)

def blog(request):
    context = []
    return render(request, 'blog.html', context)

def contact(request):
    context = []
    return render(request, 'contact.html', context)
