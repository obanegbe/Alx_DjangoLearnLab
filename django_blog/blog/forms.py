from django import forms
from .models import Post, Comment

class TagWidget(forms.TextInput):
    """
    Custom widget for handling tags.
    It will render as a simple text input but can later be extended
    (e.g., with JS for autocomplete, comma-separated tags, etc.)
    """
    def __init__(self, attrs=None):
        default_attrs = {"placeholder": "Enter tags separated by commas"}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags"]  # author will be set automatically
        widgets = {
            "tags": TagWidget(),  # 👈 use custom TagWidget
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment here..."})
        }
        
