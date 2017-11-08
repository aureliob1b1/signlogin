from django import forms
from home.models import Post

class HomeForm(forms.ModelForm): #bounded form
    your_post = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post # this is the class Post defined in models.py
        fields = ('your_post',)








# x, y = 1, 2
# x, y = (1, 2)
# x = (1, 2)
# x = (1,)
#try this in python with type(...)



#UNBOUNDED FORM to MODEL
# class HomeForm(forms.Form):
#     your_post = forms.CharField() # name of the variable is rendered in the html through the form: your_post --> Your post
