from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Index")

def about(request):
	return HttpResponse("About")

def projects(request):
	return HttpResponse("Projects")

def blog(request):
	return HttpResponse("Blog")

def contact(request):
	return HttpResponse("Contact")
