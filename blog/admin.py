from django.contrib import admin

# Register your models here.

from .models import (ThesisProject,
                     ContactUs,
                     Completation,
                     Blog,Images,
                     Author,
                     ThesisFiles,
Category,
                     Language)



admin.site.register(ContactUs)
admin.site.register(Images)





@admin.register(Completation)
class CompetetionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    # class Media:
    #     js=('tinymce.js')

@admin.register(ThesisProject)
class ThesisProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Author)
admin.site.register(ThesisFiles)
admin.site.register(Language)
admin.site.register(Category)
