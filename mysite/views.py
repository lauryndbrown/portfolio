from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from mysite.models import BlogPost
def index(request):
    context = {}
    return render(request, 'index.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def projects(request):
    context = {}
    return render(request, 'projects.html', context)

def blog(request):
    context = {}
    context["blogs"] = BlogPost.objects.filter(published=True) 
    return render(request, 'blog.html', context)

def blog_post(request, blog_post_id):
    context = {}
    context['post'] = get_object_or_404(BlogPost,id=blog_post_id)
    return render(request, 'blog_post.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)
