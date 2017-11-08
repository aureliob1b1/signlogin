from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm): #inherites methods and attributes from UserCreationForm class in django.contrib.auth.forms...
    email = forms.EmailField(required=True)

    class Meta: #config of the data inside the upperclass
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False) #
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'last_login'
        )
#tuto 16

#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example/8542030#8542030
# models.py / forms.py / views.py / urls.py
#from django import forms
# class DocumentForm(forms.Form):
#     docfile = forms.FileField(
#         label='Select a file',
#         help_text='max. 42 megabytes'
#     )
