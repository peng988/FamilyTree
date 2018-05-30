from django import forms

from .models import Post
from .models import Family

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class FamilyForm(forms.Form):
         
         
        my_code123 = forms.CharField()

class SearchForm(forms.Form):
         
         
        m_input = forms.CharField(label='', max_length=100)