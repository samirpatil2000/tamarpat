from django.shortcuts import render, redirect
from .forms import ImageForm,BlogForm
# Create your views here.

def index(request):
    return render(request,'bootstrap/')


def createSlug(title):
    slug_=""
    for i in title:
        if i!=" ":
            if ord(i)>=97:slug_+=i
            else:slug_+=chr(ord(i)+32)
        else:slug_+="-"
    return slug_

def createBlog(request):
    form=BlogForm()
    if request.method=="POST":
        form=BlogForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.slug=createSlug(blog.title)
            form.save()
            return redirect('index')
    return render(request,'')




