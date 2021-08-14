from django.urls import path
from . import views
from .models import Competition

urlpatterns = [
    path('',views.index,name='index'),
    path('thesis/',views.thesisListView,name='thesisListView'),
    path('opportunity/',views.opportunity,name='opportunity'),

    path('competition/',views.competition,name='competition'),
    path('scholarships/',views.scholarships,name='scholarships'),
    path('career/',views.career,name='career'),
    path('exams-detail/<str:slug>',views.examDetailsView,name='exams_detail'),

    path('publish/',views.publish,name='publish'),
    path('detailPage/<str:slug>',views.detailPage,name='detailPage'),
    path('detailWithIndexPage/<str:thesis_slug>/<int:id>',views.detailWithIndexPage,name='detailWithIndexPage'),
    path('authors/',views.authors,name='authors'),

    path('author/<int:id>/',views.authorDetailView,name='authors-detail'),


    # add thesis
    path('add/',views.add,name='add'),
    path('addThesis/',views.addThesisProject,name='add_thesis'),
    path('addIndex/<str:proj_slug>',views.addIndexTOThesisProject,name='add_index_to_thesis'),

    # add
    path('add/competition/',views.addCompetions,name='add_competitions'),
    path('add/scholarships/',views.addScholarship,name='add_scholarship'),
    path('add/career/',views.addCareer,name='add_career'),
    path('add/entrance-exam/',views.addEntranceExam,name='add_entrance_exam'),

    # add author
    path('add/author/',views.addAuthor,name='add_author'),

    # update
    path('u/competition/<int:id>/',views.updateCompetitions,name='edit_competition'),
    path('u/scholarships/<int:id>/',views.updateScholarship,name='edit_scholarships'),
    path('u/career/<int:id>/',views.updateCareer,name='edit_career'),
    path('u/exam/<int:id>/',views.updateExam,name='edit_exam'),

    # update
    path('u/<str:proj_slug>',views.editThesisPoject,name='edit_thesis'),
    path('u/<str:thesis_slug>/<int:id>', views.editThesisIndex, name='edit_thesisIndex'),

    # delete
    path('delete/<str:thesis_slug>/<int:index_id>',views.deleteThesisIndex,name='delete_thesisIndex'),
    path('delete/<str:thesis_slug>',views.deleteThesisProjet,name='delete_thesis'),


    path('delete/competition/<int:id>/',views.deleteCompetitions,name='delete_competition'),
    path('delete/scholarships/<int:id>/',views.deleteScholarship,name='delete_scholarships'),
    path('delete/career/<int:id>/',views.deleteCareer,name='delete_career'),
    path('delete/exam/<int:id>/',views.deleteExam,name='delete_exam'),

    path('pdf/',views.pdf,name='pdf'),
]