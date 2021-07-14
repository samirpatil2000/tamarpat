from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import ThesisFiles,Category,ThesisProject,Subscriber,Completation,Scholarship,Career
import datetime

def index(request):
    context={
        'objects':ThesisProject.objects.all()[:3],
        'english_projects':ThesisProject.objects.filter(language__name__contains="English"),
        'marathi_projects':ThesisProject.objects.filter(language__name__contains="Marathi")
    }
    if request.GET:
        query=request.GET.get('search_query')
        qs=ThesisProject.objects.all().filter(title__icontains=query)
        context['objects']=qs
    if request.POST:
        email=request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request,"Already Subscribe")
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, "Subscribe Successfully")
    return render(request,'new/index.html',context)



def author(request):
    return render(request,'new/author.html')
def opportunity(request):
    return render(request,'new/opportunity.html')

def competition(request):
    context={
        'objects':Completation.objects.all()
    }
    return render(request,'new/competition.html',context)

def scholarships(request):
    context={
        'objects':Scholarship.objects.all()
    }
    return render(request,'new/scholarship.html',context)

def career(request):
    context={
        'objects':Career.objects.all()
    }
    return render(request,'new/scholarship.html',context)


def publish(request):

    if request.POST:
        thesis_title=request.POST.get('thesis_title')
        student_name=request.POST.get('student_name')
        student_email=request.POST.get('student_email')


        ArtProjects_checkbox=request.POST.get('ArtProjects_checkbox')
        Articles_checkbox=request.POST.get('Articles_checkbox')
        Thesis_checkbox=request.POST.get('Thesis_checkbox')
        ResearchPaper_checkbox=request.POST.get('ResearchPaper_checkbox')

        Self_Photograph=request.POST.get('Self_Photograph')
        Project=request.POST.get('Project')

        Copyright_checkbox=request.POST.get('Copyright_checkbox')
        PersonalRights_checkbox=request.POST.get('PersonalRights_checkbox')

        bio=request.POST.get('bio')

        print(request.POST)

        TYPE = (
            ('Art Projects', 'Art Projects'),
            ('Articles', 'Articles'),
            ('Thesis', 'Thesis'),
            ('Research Paper', 'Research Paper'),
        )
        try:
            project=ThesisFiles.objects.create(
                title=thesis_title ,
                profile_pic=Self_Photograph ,
                full_name= student_name,
                email= student_email,
                # college_name= ,
                bio=bio ,
                document=Project,
                # google_drive_url= None,
                copyright=True,
                personal_rights=True
            )
            if ArtProjects_checkbox=="on":
                project.category.add(Category.objects.get_or_create(name=TYPE[1][0])[0])
            if Articles_checkbox=="on":
                project.category.add(Category.objects.get_or_create(name=TYPE[2][0])[0])
            if Thesis_checkbox=="on":
                project.category.add(Category.objects.get_or_create(name=TYPE[3][0])[0])
            if ResearchPaper_checkbox=="on":
                project.category.add(Category.objects.get_or_create(name=TYPE[4][0])[0])
            messages.success(request,'Successfully Create')
            return redirect('index')

        except Exception as e:
            messages.error(request, 'Something Went Wrong')
            return redirect('index')

    return render(request,'new/publish.html')

def detailPage(request,slug):
    object=ThesisProject.objects.get(slug=slug)
    context={
        'object':object
    }
    return render(request,'new/guide.html',context)

def createSlug(title):
    slug_=""
    for i in title:
        if i!=" ":
            if ord(i)>=97:slug_+=i
            else:slug_+=chr(ord(i)+32)
        else:slug_+="-"
    return slug_

# def createBlog(request):
#     form=BlogForm()
#     if request.method=="POST":
#         form=BlogForm(request.POST or None,request.FILES or None)
#         if form.is_valid():
#             blog=form.save(commit=False)
#             blog.slug=createSlug(blog.title)
#             form.save()
#             return redirect('index')
#     return render(request,'')






