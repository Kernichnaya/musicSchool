from django.urls import include, path

from . import views
 

urlpatterns = [
    path('', views.index),
#    path(r'index_page', views.index_page),
#    path('views', views.index_page),
]