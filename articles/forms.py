from xml.etree.ElementTree import Comment
from django import forms
from .models import Articles, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# class ImageForm(forms.ModelForm):
#     class Meta:serializers
#         model = Image
#         fields = ['file']
# ImageFormSet = forms.inlineformset_factory(Articles, Image, form=ImageForm, extra=3)