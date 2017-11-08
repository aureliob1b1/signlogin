from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse #dynamic urls
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    ) #custumized views inheriting from django.contrib.auth.forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm # mothers views on which are based the customized views
from django.contrib.auth import authenticate, login, update_session_auth_hash # logs user in directly after registration, keep session after changing password
from django.contrib.auth.decorators import login_required # @login_required before the function to deny it

# def home(request):
#      numbers = [1,2,3,4,5]
#      name = 'G B'
#      args = {'myName': name, 'numbers': numbers} # dictionnary where the key is a string 'myName' that will point in the template the variable name (which value is a string 'G B')
#      return render(request, 'accounts/home.html', args ) # args is what will be passed to the template through render method


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST.get('username')
            password=request.POST.get('password1')
            user=authenticate(request, username=username, password=password) # needs request ?
            login(request, user)

            return redirect(reverse('home:home'))
        #elseif not valid ?
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)
    ##check what if values in register do not match :The view accounts.views.register didn't return an HttpResponse object. It returned None instead

# @login_required #-- uncomment if not using LoginRequiredMiddleware
def view_profile(request, pk=None):
    storage = messages.get_messages(request)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'message': storage}
    return render(request, 'accounts/view_profile.html', args)

#  @login_required -- uncomment if not using LoginRequiredMiddleware
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

#  @login_required -- uncomment if not using LoginRequiredMiddleware
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your new password has been saved.')
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile')) # redirect to profile after changing the password
        # else:
        #     return redirect(reverse('accounts:change_password')) ##adapat a template to say data was invalid
    else:
        form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'accounts/change_password.html', args)
##Value Error and NOTbound if old password do not match POST = NONE to be fixed or logged as other user ?

#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example/8542030#8542030
# models.py / forms.py / views.py / urls.py
# from django.shortcuts import render_to_response
# from django.template import RequestContext
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
#
# from myproject.myapp.models import Document
# from myproject.myapp.forms import DocumentForm
#
# def list(request):
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile = request.FILES['docfile'])
#             newdoc.save()
#
#             # Redirect to the document list after POST
#             return HttpResponseRedirect(reverse('myapp.views.list'))
#     else:
#         form = DocumentForm() # A empty, unbound form
#
#     # Load documents for the list page
#     documents = Document.objects.all()
#
#     # Render list page with the documents and the form
#     return render_to_response(
#         'myapp/list.html',
#         {'documents': documents, 'form': form},
#         context_instance=RequestContext(request)
#     )
