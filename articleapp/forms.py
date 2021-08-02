from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # 클라이언트에게 입력받아야 될 요소
        fields = ['title', 'image', 'content']
