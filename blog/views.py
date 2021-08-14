from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import (ImageForm,
                    CreateThesisForm,
                    CreateThesisIndexForm,
                    CreateCompitationsForm,
                    CreateCareerForm,
                    CreateScholarshipForm,

                    UpdateThesisProjectForm,
                    UpdateThesisIndexForm,

UpdateCareerForm,UpdateCompletionForm,UpdateScholarshipForm,AddAuthorForm,CreateExamForm,UpdateExamForm
                    )

from .models import (ThesisFiles,Category,
                     ThesisProject,Subscriber,
                     Competition,Scholarship,
                     Career,ThesisIndex,Exam,
                     Author)
import datetime

def index(request):
    context={
        'objects':ThesisProject.objects.filter(is_checked=True)[:3],
        'exams':Exam.objects.filter(is_checked=True),
        'english_projects':ThesisProject.objects.filter(language__contains="English",is_checked=True)[:3],
        'marathi_projects':ThesisProject.objects.filter(language__contains="Marathi",is_checked=True)[:3]
    }
    if request.GET:
        query=request.GET.get('search_query')
        qs=ThesisProject.objects.filter(is_checked=True).filter(Q(title__icontains=query)
                                                                |Q(desc__name_of_index__icontains = query))
        context['objects']=qs
    if request.POST:
        email=request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request,"Already Subscribe")
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, "Subscribe Successfully")
    return render(request,'new/index.html',context)

def thesisListView(request):
    context={
        'objects':ThesisProject.objects.filter(is_checked=True),
    }
    if request.GET:
        query=request.GET.get('search_query')
        qs=ThesisProject.objects.filter(is_checked=True).filter(Q(title__icontains=query)
                                                                |Q(author__full_name__icontains=query))
        context['objects']=qs
    return render(request,'new/thesisListView.html',context)

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



def exam(request):
    context={
        'objects':Exam.objects.all().filter(is_checked=True)
    }
    return render(request,'new/career.html',context)
# def ListView(request,career=False,thesis=False,scholarship=False,):



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
        'object':object,
        'desc':object.desc.all().order_by('index_no')
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


def authorDetailView(request,id):
    # print(x:=[i.id for i in Author.objects.all()])
    context={
        'object':Author.objects.get(id=id),
        'objects': ThesisProject.objects.filter(is_complete=True,author__id=id)
    }
    return render(request,'new/profilePage.html',context)

def examDetailsView(request,slug):
    context={
        'object':Exam.objects.get(slug=slug)
    }
    return render(request,'new/examDetail.html',context)

def add(request):
    return render(request,'new/add.html')

def createSlug(title):
    list_=[]
    slug_=""
    import random
    for i in title:
        if i!=" ":
            if ord(i)>=97:
                slug_+=i
            elif ord(i)<=122:
                slug_ += chr(ord(i) + 32)
            else:
                x=random.randint(97,122)
                slug_+=str(chr(x))
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



def addThesisProject(request):
    form=CreateThesisForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateThesisForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.title)
            form.save()
            return redirect('edit_thesis',proj.slug)
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
            "author":current_project.author,
            "language":current_project.language,
        }
    )
    context={
        'form':update_form,
        'slug':proj_slug,
    }
    return render(request,'new/updateThesisProject.html',context)



def addCompetions(request):
    form=CreateCompitationsForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateCompitationsForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.title)
            form.save()
            return redirect('competition')
    context={
        'work': 'ADD Competition',
        'form':form,
    }
    return render(request,'new/add_new.html',context)
def addCareer(request):
    form=CreateCareerForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateCareerForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.title)
            form.save()
            return redirect('career')
    context={
        'work': 'ADD',
        'form':form,
    }
    return render(request, 'new/add_new.html', context)
def addAuthor(request):
    form=AddAuthorForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=AddAuthorForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.save()
            return redirect('authors')
    context={
        'work': 'ADD Author',
        'form':form,
    }
    return render(request, 'new/add_new.html', context)
def addScholarship(request):
    form=CreateScholarshipForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateScholarshipForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.title)
            form.save()
            return redirect('scholarships')
    context={
        'work':'ADD Scholarship',
        'form':form,
    }
    return render(request,'new/add_new.html',context)
def addEntranceExam(request):
    form=CreateExamForm()

    # if not request.user.is_authenticated:

    if request.method=="POST":
        form=CreateExamForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            proj=form.save(commit=False)
            proj.slug=createSlug(proj.title)
            form.save()
            return redirect('index')
    context={
        'work':'ADD Entrance Exam',
        'form':form,
    }
    return render(request,'new/add_new.html',context)


def updateCompetitions(request,id):
    form=UpdateCompletionForm()
    current_object=Competition.objects.get(id=id)
    if request.method=="POST":
        form=UpdateCompletionForm(request.POST or None,request.FILES or None,instance=current_object)
        if form.is_valid():
            update=form.save(commit=False)
            update.save()
            return redirect('competition')

    form=UpdateCompletionForm(
        initial={
            "title":current_object.title,
            "thumbnail":current_object.thumbnail,
            "is_checked":current_object.is_checked,
            "is_complete":current_object.is_complete,
            "desc":current_object.desc,
            "url":current_object.url,
            "acceptedMedia":current_object.acceptedMedia,
            "eligibility":current_object.eligibility,
            "deadline":current_object.deadline,
        }
    )
    context={
        'work':'Update Competition',
        'form':form,
        'id': id,
        'url': 'delete_competition'
    }
    return render(request,'new/add_new.html',context)
def updateScholarship(request,id):
    form=UpdateScholarshipForm()
    current_object=Scholarship.objects.get(id=id)
    if request.method=="POST":
        form=UpdateScholarshipForm(request.POST or None,request.FILES or None,instance=current_object)
        if form.is_valid():
            update=form.save(commit=False)
            update.save()
            return redirect('scholarships')

    form=UpdateScholarshipForm(
        initial={
            "title":current_object.title,
            "thumbnail":current_object.thumbnail,
            "is_checked":current_object.is_checked,
            "is_complete":current_object.is_complete,
            "desc":current_object.desc,
            "url":current_object.url,
        }
    )
    context={
        'work':'Update Scholarship',
        'form':form,
        'id': id,
        'url': 'delete_scholarships'
    }
    return render(request,'new/add_new.html',context)
def updateCareer(request,id):
    form=UpdateCareerForm()
    current_object=Career.objects.get(id=id)
    if request.method=="POST":
        form=UpdateCareerForm(request.POST or None,request.FILES or None,instance=current_object)
        if form.is_valid():
            update=form.save(commit=False)
            update.save()
            return redirect('career')

    form=UpdateCareerForm(
        initial={
            "title":current_object.title,
            "thumbnail":current_object.thumbnail,
            "is_checked":current_object.is_checked,
            "is_complete":current_object.is_complete,
            "desc":current_object.desc,
            "url":current_object.url,
        }
    )
    context={
        'work':'Update Career',
        'form':form,
        'id': id,
        'url': 'delete_career'
    }
    return render(request, 'new/add_new.html', context)
def updateExam(request, id):
    form = UpdateExamForm()
    current_object = Exam.objects.get(id=id)
    if request.method == "POST":
        form = UpdateExamForm(request.POST or None, request.FILES or None, instance=current_object)
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            return redirect('exams_detail', update.slug)

    form = UpdateExamForm(
        initial={
            "title": current_object.title,
            "is_checked": current_object.is_checked,
            "is_complete": current_object.is_complete,
            "desc": current_object.desc,
            "url": current_object.url,
        }
    )

    context = {
        'work': 'Update Entrance Exam',
        'form': form,
        'id': id,
        'url': 'delete_exam'
    }
    return render(request, 'new/add_new.html', context)

def deleteThesisProjet(request,thesis_slug):
    # try:
        obj=ThesisProject.objects.get(slug=thesis_slug)
        for o in obj.desc.all():
            idx=ThesisIndex.objects.get(id=o.id)
            idx.delete()
        obj.delete()
        return redirect('thesisListView')
    # except Exception as e:
    #     return redirect('thesisListView')

def deleteCompetitions(request,id,Object):
    current_object=Object.objects.get(id=id)
    current_object.delete()
    return redirect('index')
def deleteScholarship(request,id):
    current_object=Scholarship.objects.get(id=id)
    current_object.delete()
    return redirect('index')
def deleteCareer(request,id):
    current_object=Career.objects.get(id=id)
    current_object.delete()
    return redirect('index')
def deleteExam(request, id):
    current_object = Exam.objects.get(id=id)
    current_object.delete()
    return redirect('index')



#TO REMOVE
def deleteThesisIndex(request,thesis_slug,index_id):
    try:
        obj=ThesisIndex.objects.get(id=index_id)
        obj.delete()
        return redirect('detailPage',thesis_slug)
    except Exception as e:
        return redirect('detailPage',thesis_slug)

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
        'work': 'Update',
        'form':update_form,
        'slug':thesis_slug,
        'id':id,
    }
    return render(request, 'new/NotInUse/updateThesisIndex.html', context)
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
    return render(request, 'new/NotInUse/addIndexTOThesis.html', context)


def pdf(request):
    obj=ThesisProject.objects.filter(id=30)[0]
    context={
        'pdf_':'https://www.ph.ucla.edu/epi/rapidsurveys/RScourse/RSbook_ch3.pdf',
        'pdf_2':obj.pdf,
    }
    return render(request,'new/control_pdf.html',context)

def pdf2(request):
    obj=ThesisProject.objects.filter(id=30)[0]
    context={
        'pdf_':obj.pdf
    }
    return render(request,'new/pdf.html',context)