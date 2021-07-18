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

]