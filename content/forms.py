from django import forms
from .models import User,Document,Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment;
        fields=('content','user','doc')