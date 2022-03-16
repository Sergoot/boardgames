from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {'text': Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш комментарий',
                'id': 'inputPassword5',
                'aria-describedby': 'passwordHelpBlock',
            }
        )}
