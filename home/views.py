from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm
from home.models import Post, Friend


class HomeView(TemplateView): #HomeView inherites from TemplateView (thier is the render)
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        #users = User.objects.all() # get other users
        users = User.objects.exclude(id=request.user.id)
        friend, created = Friend.objects.get_or_create(current_user=request.user)
        friends = friend.users.all()

        args = {
            'form':form, 'posts': posts, 'users': users, 'friends': friends
        }# pass all objects to the template
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST) #give the variable the values that have been posted - request.POST
        if form.is_valid():
            post = form.save(commit=False) # saves form into post
            post.user = request.user # associate user and post
            post.save()
            text = form.cleaned_data['your_post'] #security that clean data from malicious elements
            form = HomeForm() # blanks form after sumit
            return redirect('home:home') # redirect intead of rendering in the same webpage

        args = {'form': form, 'text':text} # variables (with values of form and text) that will be pass through the methd for rendering in the template
        return render(request, self.template_name, args)

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')


#SIMPLEST TEST VIEW
# from django.shortcuts import render
# from django.http import HttpResponse
#
# def home(request):
#     return HttpResponse('it works')
