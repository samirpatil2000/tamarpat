
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
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

    def __str__(self):
        return self.full_name

class BaseModel(models.Model):
    title=models.CharField(max_length=100,default="Title")
    desc=RichTextField(default="Text here",blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    thumbnail=models.ImageField(upload_to='media',blank=True,default='no-image.jpg')
    slug=models.SlugField(unique=True,blank=True,null=True)

    def __str__(self):
        return self.title

class Blog(BaseModel):
    images=models.ManyToManyField(Images,blank=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)


class Completation(BaseModel):
    url=models.URLField(blank=True,null=True)


class ThesisProject(BaseModel):
    document=models.FileField(upload_to='media/pdf/',blank=True)
    google_drive_url=models.URLField(blank=True,null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)

class ContactUs(models.Model):
    full_name = models.CharField(max_length=50,default="Your Name")
    email = models.EmailField(max_length=100,default="example@gmail.com")
    query = models.TextField()

    def __str__(self):
        return self.full_name

