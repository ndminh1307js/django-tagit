from django import forms

from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image', ]
        labels = {
            'caption': '',
            'image': 'Upload your image (optional)'
        }
        widgets = {
            'caption': forms.Textarea(attrs={'placeholder': 'What do you feel today?'})
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
        labels = {
            'content': ''
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your comment'})
        }
