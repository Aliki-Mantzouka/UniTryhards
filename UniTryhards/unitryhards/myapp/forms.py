from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from .models import Paper

# Custom UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only the comment text is needed from the user

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'placeholder': 'Add a comment...', 'class': 'form-control'})
        
class PaperUploadForm(forms.ModelForm):
    class Meta:
        model = Paper
        fields = ['title', 'description', 'file', 'category', 'course']