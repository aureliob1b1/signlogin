from django.conf.urls import url
from home.views import HomeView # from home/view.py import the class indicated
from . import views


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'), # resolve the url passing the HomeView class and inherites a method - as_view from - from an other class  // url resolver needs a function not a class
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]
