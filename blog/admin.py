from django.contrib import admin

# Register your models here.

from .models import ThesisProject,ContactUs,Completation,Blog,Images



admin.site.register(ContactUs)
admin.site.register(Images)





@admin.register(Completation)
class CompetetionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


@admin.register(ThesisProject)
class ThesisProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

