from django import forms
from .models import post,category,Comment



# choices=[('coding','coding'),('sports','sports'),('entertiment','entertiment')]
choices = category.objects.all().values_list('name','name')
choice_list =[]
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title', 'author','category', 'body','header_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':choices}),
            'author': forms.Select(attrs={'class': 'form-control'}),
             'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
