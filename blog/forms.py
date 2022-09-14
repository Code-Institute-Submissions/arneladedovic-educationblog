from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for adding comment
    """
    class Meta:
        model = Comment
        fields = ('body',)