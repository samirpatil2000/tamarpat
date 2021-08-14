from django.contrib import admin

# Register your models here.

from .models import (ThesisProject,
                     ContactUs,
                     Competition,
                     Blog, Images,
                     Author,
                     ThesisFiles,
                     Category,
                     Subscriber,
                     Scholarship,
                     Career,
                    Exam,
                    ThesisIndex,
                    Type,
                    Constant
                     )



admin.site.register(ContactUs)
admin.site.register(Images)





@admin.register(Competition)
class CompetetionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('title',)}
    # class Media:
    #     js=('tinymce.js')

@admin.register(ThesisProject)
class ThesisProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Author)
admin.site.register(ThesisFiles)
admin.site.register(Category)
admin.site.register(Exam)


admin.site.register(Subscriber)

@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ThesisIndex)
admin.site.register(Type)
admin.site.register(Constant)

