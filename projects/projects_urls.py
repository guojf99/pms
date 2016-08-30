from django.conf.urls import url
from . import views

app_name='projects'
urlpatterns = [
    url(r'^hello$', views.hello),
    #url(r'^ajax$', views.ajax),
    url(r'^$', views.index, name='index'),
]