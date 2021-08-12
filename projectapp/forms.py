from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        # form 적용시킬 대상
        model = Project
        # 클라이언트에게 입력받을 요소 정하기
        fields = ['name', 'image', 'description']