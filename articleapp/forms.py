from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    # models.py에서는 models.~~였다면 forms.py에서는 forms.~~로 시작
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'text-align: left;'
                                                                    'min-height: 10rem;'}))

    class Meta:
        model = Article
        # 클라이언트에게 입력받아야 될 요소
        fields = ['title', 'image', 'project', 'content']
