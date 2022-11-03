from django import forms
from .models import Articles, Comment, Category



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'content', 'image', 'category')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content": " ",
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields["content"].widget.attrs = {
            "class": "form-control me-3",
            "placeholder": "댓글을 입력해주세요",
            "rows": 1,
        }


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ['file']
# ImageFormSet = forms.inlineformset_factory(Articles, Image, form=ImageForm, extra=3)
