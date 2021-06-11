from django.contrib import admin
from django.urls import path
from .  import views



urlpatterns = [
    path('',views.home),
    path('cours/',views.cours),
    path("<slug:slug>",views.content,name='content'),
    path("about/",views.about,name='about'),
    path("<slug:slug>/devoir",views.devoir,name='devoir'),
    path("<slug:slug>/exam",views.exam,name="exam"),
    path("driss/",views.comments),
    path("render/",views.rendre),
    path("<slug:slug>/annoce",views.annoce),
 
]