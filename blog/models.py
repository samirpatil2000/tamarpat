
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

from django.core.validators import MaxValueValidator,MinValueValidator

user=settings.AUTH_USER_MODEL
# Create your models here.
class Images(models.Model):
    image=models.ImageField(upload_to='media',blank=True)

class Author(models.Model):
    # user=models.OneToOneField(user,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='ProfilePics', default="avatar.svg")
    full_name=models.CharField(max_length=100,default="Full Name")
    college_name=models.CharField(max_length=100,default="College Name",blank=True,null=True)
    date_of_birth=models.DateField(blank=None,null=True)
    bio=models.TextField(blank=True,null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):return self.full_name

class BaseModel(models.Model):
    title=models.CharField(max_length=200,default="Title")
    date=models.DateTimeField(auto_now_add=True)
    thumbnail=models.ImageField(upload_to='media',blank=True,default='no-image.jpg')
    slug=models.SlugField(unique=True,blank=True,null=True)
    is_checked=models.BooleanField(default=True)
    is_complete=models.BooleanField(default=True)

    def __str__(self):return self.title

    def get_absolute_url(self):
        return reverse('detailPage',kwargs={'slug':self.slug})

class Blog(BaseModel):
    desc = RichTextField(default="Text here", blank=True, null=True)
    images=models.ManyToManyField(Images,blank=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)


class Competition(BaseModel):
    desc = RichTextField(default="Text here", blank=True, null=True)
    url=models.URLField(blank=True,null=True)
    acceptedMedia=models.TextField(blank=True,null=True)
    eligibility=models.TextField(blank=True,null=True)
    deadline=models.TextField(blank=True,null=True)

    class Meta:
        verbose_name_plural="Competition's"

class ThesisIndex(models.Model):
    index_no=models.IntegerField(blank=True,null=True
                                 ,validators=[MinValueValidator(0),MaxValueValidator(50)]
                                 )
    name_of_index = models.CharField(max_length=100,default="Title")
    content = RichTextField(default='content here', blank=True, null=True)

    def __str__(self):
        return self.name_of_index

    class Meta:
        verbose_name_plural="ThesisIndex's"

class Scholarship(BaseModel):
    desc = RichTextField(default="Text here", blank=True, null=True)
    url=models.URLField(blank=True,null=True)
    class Meta:
        verbose_name_plural="Scholarship's"

class Career(BaseModel):
    desc = RichTextField(default="Text here", blank=True, null=True)
    url=models.URLField(blank=True,null=True)
    class Meta:
        verbose_name_plural="Career's"

LANGUAGE = (
    ('English', 'English'),
    ('Marathi', 'Marathi'),
)

class ThesisProject(BaseModel):
    headline=RichTextField(default="Headline here",blank=True,null=True)
    desc = models.ManyToManyField(ThesisIndex,blank=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    language=models.CharField(choices=LANGUAGE,max_length=10,default=LANGUAGE[0][0])

    class Meta:
        verbose_name_plural="Thesis Project's"

TYPE = (
    ('Art Projects', 'Art Projects'),
    ('Articles', 'Articles'),
    ('Thesis', 'Thesis'),
    ('Research Paper', 'Research Paper'),
)

class Category(models.Model):
    name=models.CharField(choices=TYPE,max_length=20,unique=True)

    def __str__(self):return self.name


    class Meta:
        verbose_name_plural="Category Of Projects"

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

    class Meta:
        verbose_name_plural="Thesis Uploaded By User"


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50,default="Your Name")
    email = models.EmailField(max_length=100,default="example@gmail.com")
    query = models.TextField()

    def __str__(self):return self.full_name

    class Meta:
        verbose_name_plural="Contact Messages"

class Subscriber(models.Model):
    email = models.EmailField(max_length=100, default="example@gmail.com",unique=True)


    def __str__(self):return self.email

    class Meta:
        verbose_name_plural="Subscriber's"