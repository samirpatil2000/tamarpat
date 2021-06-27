from django import  forms

from .models import Blog,Images,ThesisProject




class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model=Images
        fields='__all__'

class ThesisForm(forms.ModelForm):
    class Meta:
        model=ThesisProject
        fields="__all__"
