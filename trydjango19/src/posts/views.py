from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_create(request):
	return HttpResponse("create link")

def post_detail(request):
	return render(request, "index.html", {})

def post_update(request):
	return HttpResponse("update link")

def post_delete(request):
	return HttpResponse("delete link")
