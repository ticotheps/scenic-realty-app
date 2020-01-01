# this 'path' import is required to provide a URL for the pages app
from django.urls import path 
# this 'views' import is required to connect our new URL to its views
from . import views 


urlpatterns = [
  # (<root path for home page>, <method to connect to>, <name used to access
  # this path>)
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
]