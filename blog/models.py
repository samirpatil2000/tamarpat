
from django.db import models

# Create your models here.
class Images(models.Model):
    image=models.ImageField(upload_to='media',blank=True)


class BaseModel(models.Model):
    title=models.CharField(max_length=100,default="Title")
    desc=models.TextField(default="Text here",blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    thumbnail=models.ImageField(upload_to='media',blank=True,default='no-image.jpg')
    author=models.CharField(max_length=10,blank=True,null=True)
    slug=models.SlugField(unique=True,blank=True,null=True)
    def __str__(self):
        return self.title

class Blog(BaseModel):
    images=models.ManyToManyField(Images,blank=True)


class Completation(BaseModel):
    url=models.URLField(blank=True,null=True)


class ThesisProject(BaseModel):
    document=models.FileField(upload_to='media/pdf/',blank=True)
    google_drive_url=models.URLField(blank=True,null=True)

class ContactUs(models.Model):
    full_name = models.CharField(max_length=50,default="Your Name")
    email = models.EmailField(max_length=100,default="example@gmail.com")
    query = models.TextField()

    def __str__(self):
        return self.full_name

