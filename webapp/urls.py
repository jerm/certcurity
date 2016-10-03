from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^goo$', views.index, name='indexgoogoo'),
    url(r'^FilesForm', views.FormWithFilesView,name='form')
    #url(r'/', views.index, name='index'),
]
