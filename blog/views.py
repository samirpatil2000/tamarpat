from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import (ImageForm,
                    CreateThesisForm,
                    CreateThesisIndexForm,
                    CreateCompitationsForm,
CreateCareerForm,CreateScholarshipForm,
                    UpdateThesisProjectForm,
                    UpdateThesisIndexForm
                    )

from .models import (ThesisFiles,Category,
                     ThesisProject,Subscriber,
                     Competition,Scholarship,
                     Career,ThesisIndex,
                     Author)
import datetime

def index(request):
    context={
        'objects':ThesisProject.objects.filter(is_checked=True)[:3],
        'english_projects':ThesisProject.objects.filter(language__contains="English",is_checked=True),
        'marathi_projects':ThesisProject.objects.filter(language__contains="Marathi",is_checked=True)
    }
    if request.GET:
        query=request.GET.get('search_query')
        qs=ThesisProject.objects.all().filter(title__icontains=query,is_checked=True)
        context['objects']=qs
    if request.POST:
        email=request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request,"Already Subscribe")
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, "Subscribe Successfully")
    return render(request,'new/index.html',context)

def opportunity(request):
    return render(request,'new/opportunity.html')

def competition(request):
    context={
        'objects':Competition.objects.all().filter(is_checked=True)
    }
    return render(request,'new/competition.html',context)

def scholarships(request):
    context={
        'objects':Scholarship.objects.all().filter(is_checked=True)
    }
    return render(request,'new/scholarship.html',context)

def career(request):
    context={
        'objects':Career.objects.all().filter(is_checked=True)
    }
    return render(request,'new/career.html',context)


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
    return render(request, 'new/thesisDetail.html', context)


def detailWithIndexPage(request,thesis_slug:str,id:int):
    thesis = ThesisProject.objects.get(slug=thesis_slug)
    object=ThesisIndex.objects.get(pk=id)
    context={
        'object':object,
        'thesis':thesis
    }
    return render(request,'new/indexDetail.html',context)


def authors(request):
    context={
        'objects':Author.objects.all().filter(is_active=True)
    }
    return  render(request,'new/author.html',context)


def authorDetailView(request,email):
    context={
        'user':Author.objects.get(user__email=email)
    }
    return render(request,'new/author.html')

def add(request):
    return render(request,'new/add.html')

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


def addIndexTOThesisProject(request,proj_slug):
    project=ThesisProject.objects.get(slug=proj_slug)
    form=CreateThesisIndexForm()

    if request.POST:
        form=CreateThesisIndexForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            index=form.save(commit=False)
            index.save()
            project.desc.add(index)
            return redirect('detailPage',proj_slug)
    context={
        'form':form,
        'slug':proj_slug,
        'project':project,
    }
    return render(request,'new/addIndexTOThesis.html',context)

def addThesisProject(request):
    form=CreateThesisForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateThesisForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.title)
            form.save()
            return redirect('detailPage',proj.slug)
    context={
        'form':form,
    }
    return render(request,'new/addThesisProject.html',context)

def editThesisPoject(request,proj_slug):
    update_form=UpdateThesisProjectForm()
    current_project=ThesisProject.objects.get(slug=proj_slug)
    if request.POST:
        update_form=UpdateThesisProjectForm(request.POST or None,request.FILES or None,instance=current_project)
        if update_form.is_valid():
            proj=update_form.save(commit=False)
            proj.save()
            return redirect('detailPage',proj_slug)

    update_form=UpdateThesisProjectForm(
        initial={
            "title":current_project.title,
            "thumbnail":current_project.thumbnail,
            "is_checked":current_project.is_checked,
            "is_complete":current_project.is_complete,
            "headline":current_project.headline,
            "author":current_project.author,
            "language":current_project.language,
        }
    )
    context={
        'form':update_form,
    }
    return render(request,'new/updateThesisProject.html',context)

def editThesisIndex(request,thesis_slug,id):
    update_form=UpdateThesisIndexForm()
    current_index=ThesisIndex.objects.get(id=id)

    if request.POST:
        update_form=UpdateThesisIndexForm(request.POST or None,request.FILES or None,instance=current_index)
        if update_form.is_valid():
            index=update_form.save(commit=False)
            index.save()
            return redirect('detailPage',thesis_slug)
    update_form=UpdateThesisIndexForm(
        initial={
            "index_no":current_index.index_no,
            "name_of_index":current_index.name_of_index,
            "content":current_index.content,
        }
    )
    context={
        'form':update_form
    }
    return render(request,'new/updateThesisIndex.html',context)

def addCompetions(request):
    form=CreateCompitationsForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateCompitationsForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.name_of_index)
            form.save()
            return redirect('competition')
    context={
        'form':form,
    }
    return render(request,'new/addCompetation.html',context)


def addCareer(request):
    form=CreateCareerForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateCareerForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.name_of_index)
            form.save()
            return redirect('career')
    context={
        'form':form,
    }
    return render(request,'new/addCareers.html',context)


def addScholarship(request):
    form=CreateScholarshipForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateScholarshipForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.name_of_index)
            form.save()
            return redirect('scholarships')
    context={
        'form':form,
    }
    return render(request,'new/addSchorships.html',context)