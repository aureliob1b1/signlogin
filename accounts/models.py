#class Category(models.Model):
#    class Meta:
#        verbose_name_plural = "YourClassInPLural ex: categories not categorys"
#AFTER CHANGING A MODEL -> MAKEMIGRATIONS in the DB every single time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# class UserProfileManager(models.Manager):
#     def get_queryset(self):
#         return super(UserProfileManager, self).get_queryset().filter(city='')

class UserProfile(models.Model): #inherites models from Model
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    # paris = UserProfileManager()
    # objects = models.Manager() #bux fix 1

    def __str__(self):
        return self.user.username # to get user profile with user name

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example/8542030#8542030
# models.py / forms.py / views.py / urls.py
# from django.db import models
#
# class Document(models.Model):
#     docfile = models.FileField(upload_to='documents/%Y/%m/%d')
