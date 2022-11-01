from xml.etree.ElementTree import Comment
from django import forms
from .models import Articles, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']