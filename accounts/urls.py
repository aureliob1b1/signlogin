from django.conf.urls import url
from . import views # needs views.some_function in the url and it looks in all folders so reference to views in other apps is possible
from django.contrib.auth.views import (  #builtin views in Django
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)
urlpatterns = [
    #url(r'^$', views.home, name='home'), #r'^$' root url plugged to parent url / template without name loaded from accounts/views.py
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'), #template loaded not from the views.py but directly from url.py
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'), #template_name - default django template substituted with customized one accounts/...html
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),

    url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
]
