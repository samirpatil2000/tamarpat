from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('opportunity/',views.opportunity,name='opportunity'),
    path('competition/',views.competition,name='competition'),
    path('scholarships/',views.scholarships,name='scholarships'),
    path('career/',views.career,name='career'),
    path('publish/',views.publish,name='publish'),
    path('detailPage/<str:slug>',views.detailPage,name='detailPage'),
    path('detailWithIndexPage/<str:thesis_slug>/<int:id>',views.detailWithIndexPage,name='detailWithIndexPage'),
    path('authors/',views.authors,name='authors'),

    # add thesis

    path('addThesis/',views.addThesisProject,name='add_thesis'),
    path('addIndex/<str:proj_slug>',views.addIndexTOThesisProject,name='add_index_to_thesis'),

    # update
    path('u/<str:proj_slug>',views.editThesisPoject,name='edit_thesis'),
    path('u/<str:thesis_slug>/<int:id>', views.editThesisIndex, name='edit_thesisIndex'),

]