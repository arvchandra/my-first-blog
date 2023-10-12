from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

    def clean_title(self):
        title = self.cleaned_data['title']

        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError('Post with same title already exists.')
        
        return title
        
    def clean(self):
        cleaned_data = super().clean()

        if not ('title' in cleaned_data or 'text' in cleaned_data):
            pass
        else:
            title = self.cleaned_data['title']
            text = self.cleaned_data['text']
            if title == text:
                raise forms.ValidationError('Title and text cannot be the same.')
            
        return cleaned_data
        
