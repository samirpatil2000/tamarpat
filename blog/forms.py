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

class UpdateThesisProjectForm(forms.ModelForm):
    class Meta:
        model=ThesisProject
        fields = "__all__"
        exclude = ('desc', 'slug','date')

    def save(self, commit=True):
        proj=self.instance
        proj.title=self.cleaned_data['title']
        # proj.date=self.cleaned_data['date']
        proj.thumbnail=self.cleaned_data['thumbnail']
        proj.is_checked=self.cleaned_data['is_checked']
        proj.is_complete=self.cleaned_data['is_complete']
        proj.headline=self.cleaned_data['headline']
        proj.author=self.cleaned_data['author']
        proj.language=self.cleaned_data['language']

        if commit:
            proj.save()
        return proj

class UpdateThesisIndexForm(forms.ModelForm):
    class Meta:
        model=ThesisIndex
        fields = '__all__'

    def save(self, commit=True):
        index=self.instance
        index.index_no=self.cleaned_data['index_no']
        index.name_of_index=self.cleaned_data['name_of_index']
        index.content=self.cleaned_data['content']

        if commit:
            index.save()
        return index
