from django.shortcuts import render, redirect
from .forms import ImageForm,BlogForm
# Create your views here.


def index(request):
    return render(request,'new/index.html')
def author(request):
    return render(request,'new/author.html')
def opportunity(request):
    return render(request,'new/opportunity.html')
def publish(request):
    return render(request,'new/publish.html')

def detailPage(request):
    return render(request,'new/guide.html')
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




