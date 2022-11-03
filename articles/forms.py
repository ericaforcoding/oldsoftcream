from django import forms
from .models import Articles, Comment, Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'content', 'image', 'category')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['file']
# ImageFormSet = forms.inlineformset_factory(Articles, Image, form=ImageForm, extra=3)