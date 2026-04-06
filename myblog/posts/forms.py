from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'published']

        # HTML input larni chiroyli qilish uchun widget larni sozlash
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post sarlavhasi'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL uchun slug'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post matni'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'title': 'Sarlavha',
            'content': 'Matn',
            'published': 'Nashr qilingan',
        }