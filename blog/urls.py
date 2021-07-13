from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('author/',views.author,name='author'),
    path('opportunity/',views.opportunity,name='opportunity'),
    path('publish/',views.publish,name='publish'),
    path('detailPage/',views.detailPage,name='detailPage')

]