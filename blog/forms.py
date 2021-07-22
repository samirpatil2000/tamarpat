from django import  forms

from .models import Blog, Images, ThesisProject, ThesisIndex, Competition, Scholarship, Career,Author


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


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields="__all__"

class UpdateAuthor(forms.ModelForm):
    class Meta:
        model=Author
        fields="__all__"
    def save(self, commit=True):
        obj=self.instance
        obj.profile_pic=self.instance['profile_pic']
        obj.full_name=self.instance['full_name']
        obj.college_name=self.instance['college_name']
        obj.date_of_birth=self.instance['date_of_birth']
        obj.bio=self.instance['bio']
        obj.is_active=self.instance['is_active']

        if commit:
            obj.save()
        return obj

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

class CreateCompitationsForm(forms.ModelForm):
    class Meta:
        model=Competition
        fields='__all__'
        exclude = ('date','slug')

class CreateScholarshipForm(forms.ModelForm):
    class Meta:
        model=Scholarship
        fields='__all__'
        exclude = ('date','slug')


class CreateCareerForm(forms.ModelForm):
    class Meta:
        model=Career
        fields='__all__'
        exclude = ('date','slug')

class UpdateCompletionForm(forms.ModelForm):
    class Meta:
        model=Competition
        fields='__all__'
        exclude = ('date','slug')

    def save(self, commit=True):
        obj = self.instance
        obj.title=self.cleaned_data['title']
        obj.thumbnail=self.cleaned_data['thumbnail']
        obj.is_checked=self.cleaned_data['is_checked']
        obj.is_complete=self.cleaned_data['is_complete']
        obj.desc=self.cleaned_data['desc']
        obj.url=self.cleaned_data['url']
        obj.acceptedMedia=self.cleaned_data['acceptedMedia']
        obj.eligibility=self.cleaned_data['eligibility']
        obj.deadline=self.cleaned_data['deadline']

        if commit:
            obj.save()
        return obj

class UpdateScholarshipForm(forms.ModelForm):
    class Meta:
        model=Scholarship
        fields='__all__'
        exclude = ('date','slug')

    def save(self, commit=True):
        obj = self.instance
        obj.title=self.cleaned_data['title']
        obj.thumbnail=self.cleaned_data['thumbnail']
        obj.is_checked=self.cleaned_data['is_checked']
        obj.is_complete=self.cleaned_data['is_complete']
        obj.desc=self.cleaned_data['desc']
        obj.url=self.cleaned_data['url']

        if commit:
            obj.save()
        return obj

class UpdateCareerForm(forms.ModelForm):
    class Meta:
        model=Career
        fields='__all__'
        exclude = ('date','slug')

    def save(self, commit=True):
        obj = self.instance
        obj.title=self.cleaned_data['title']
        obj.thumbnail=self.cleaned_data['thumbnail']
        obj.is_checked=self.cleaned_data['is_checked']
        obj.is_complete=self.cleaned_data['is_complete']
        obj.desc=self.cleaned_data['desc']
        obj.url=self.cleaned_data['url']

        if commit:
            obj.save()
        return obj