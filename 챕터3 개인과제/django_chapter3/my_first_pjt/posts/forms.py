from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']  # author 필드 제외
        exclude = ("author",) # 그 중에 제외할 필드 지정


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        exclude = ("post",) # 아티클은 제외
