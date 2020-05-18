from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image']
        labels = {
            'caption': '',
            'image': 'Upload your image (optional)'
        }
        widgets = {
            'caption': forms.Textarea(attrs={'placeholder': 'What do you feel today?'})
        }
