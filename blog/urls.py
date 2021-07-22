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
    path('add/',views.add,name='add'),
    path('addThesis/',views.addThesisProject,name='add_thesis'),
    path('addIndex/<str:proj_slug>',views.addIndexTOThesisProject,name='add_index_to_thesis'),

    # add
    path('add/competition/',views.addCompetions,name='add_competitions'),
    path('add/scholarships/',views.addScholarship,name='add_scholarship'),
    path('add/career/',views.addCareer,name='add_career'),

    # add author
    path('add/author/',views.addAuthor,name='add_author'),

    # update
    path('u/competition/<int:id>/',views.updateCompetitions,name='edit_competition'),
    path('u/scholarships/<int:id>/',views.updateScholarship,name='edit_scholarships'),
    path('u/career/<int:id>/',views.updateCareer,name='edit_career'),

    # update
    path('u/<str:proj_slug>',views.editThesisPoject,name='edit_thesis'),
    path('u/<str:thesis_slug>/<int:id>', views.editThesisIndex, name='edit_thesisIndex'),



]