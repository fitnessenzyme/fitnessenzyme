# blogs/forms.py
from django import forms
from .models import Blog, Comment
from django_ckeditor_5.widgets import CKEditor5Widget

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Blog
        fields = ['title', 'post_type', 'content', 'cover_image', 'video_url', 'video_file']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'})
        }

