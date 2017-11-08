import re

from django.conf import settings
from django.urls import reverse #dynamic urls
from django.shortcuts import redirect
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware: #a function is passed to a class
    def __init__(self, get_response): # all methods in a class take self as parameter
        self.get_response = get_response #put get_response as an attributes on that object passed as parameter to a class....

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        print(request)
        path = request.path_info.lstrip('/')
        print(path)
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        #if path == 'account/logout/':
            #logout(request)
        if path == reverse('accounts:logout').lstrip('/'): #lstrip takes out the / of the url tuto 29 + namespace 31
            logout(request)

        if request.user.is_authenticated() and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated() or url_is_exempt:
            return None

        else:
            return redirect(settings.LOGIN_URL)
