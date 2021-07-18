from django import  forms

from .models import Blog,Images,ThesisProject,ThesisIndex




class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model=Images
        fields='__all__'

class CreateThesisIndexForm(forms.ModelForm):
    class Meta:
        model=ThesisIndex
        fields='__all__'

class CreateThesisForm(forms.ModelForm):
    class Meta:
        model=ThesisProject
        fields="__all__"
        exclude=('desc','slug')
