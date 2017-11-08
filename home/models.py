from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    your_post = models.CharField(max_length=500)
    user = models.ForeignKey(User) #associate a user
    created = models.DateTimeField(auto_now_add=True) # date of creation of the object not the updates
    updated = models.DateTimeField(auto_now=True) # to do put a button to update the post

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(current_user=current_user)
        friend.users.remove(new_friend)
