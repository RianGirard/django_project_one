from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return index(request)

def show(request, blog_num):
    return HttpResponse(f"placeholder to display blog number: {blog_num}")

def edit(request, blog_num):
    return HttpResponse(f"placeholder to edit blog number: {blog_num}")

def destroy(request, blog_num):
    return index(request)

# Create your views here. 
