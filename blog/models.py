
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

user=settings.AUTH_USER_MODEL
# Create your models here.
class Images(models.Model):
    image=models.ImageField(upload_to='media',blank=True)

class Author(models.Model):
    user=models.OneToOneField(user,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='ProfilePics', default="avatar.svg")
    full_name=models.CharField(max_length=100,default="Full Name")
    college_name=models.CharField(max_length=100,default="College Name",blank=True,null=True)
    date_of_birth=models.DateField(blank=None,null=True)
    bio=models.TextField(blank=True,null=True)

    def __str__(self):return self.full_name

class BaseModel(models.Model):
    title=models.CharField(max_length=100,default="Title")
    desc=RichTextField(default="Text here",blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    thumbnail=models.ImageField(upload_to='media',blank=True,default='no-image.jpg')
    slug=models.SlugField(unique=True,blank=True,null=True)

    def __str__(self):return self.title

    def get_absolute_url(self):
        return reverse('detailPage',kwargs={'slug':self.slug})

class Blog(BaseModel):
    images=models.ManyToManyField(Images,blank=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)


class Completation(BaseModel):
    url=models.URLField(blank=True,null=True)
    acceptedMedia=models.TextField(blank=True,null=True)
    eligibility=models.TextField(blank=True,null=True)
    deadline=models.TextField(blank=True,null=True)



class Scholarship(BaseModel):
    url=models.URLField(blank=True,null=True)

class Career(BaseModel):
    url=models.URLField(blank=True,null=True)

class Language(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):return self.name

class ThesisProject(BaseModel):
    headline=RichTextField(default="Headline here",blank=True,null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    language=models.ForeignKey(Language,blank=True,null=True,on_delete=models.SET_NULL)


TYPE = (
    ('Art Projects', 'Art Projects'),
    ('Articles', 'Articles'),
    ('Thesis', 'Thesis'),
    ('Research Paper', 'Research Paper'),
)

class Category(models.Model):
    name=models.CharField(choices=TYPE,max_length=20,unique=True)

    def __str__(self):return self.name


class ThesisFiles(models.Model):
    title = models.CharField(max_length=100, default="Title")
    profile_pic = models.ImageField(upload_to='ProfilePics', default="avatar.svg")
    full_name = models.CharField(max_length=100, default="Full Name")
    email = models.EmailField(max_length=100,default="example@gmail.com")
    college_name = models.CharField(max_length=100, default="College Name", blank=True, null=True)
    bio=models.TextField(blank=True,null=True)
    document = models.FileField(upload_to='media/pdf/',blank=True)
    google_drive_url = models.URLField(blank=True,null=True)
    copyright = models.BooleanField(default=False)
    personal_rights=models.BooleanField(default=False)
    category=models.ManyToManyField(Category,blank=True)

    def __str__(self):return self.title+"-"+self.full_name


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50,default="Your Name")
    email = models.EmailField(max_length=100,default="example@gmail.com")
    query = models.TextField()

    def __str__(self):return self.full_name

class Subscriber(models.Model):
    email = models.EmailField(max_length=100, default="example@gmail.com",unique=True)


    def __str__(self):return self.email