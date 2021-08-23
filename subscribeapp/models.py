from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscription', null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    class Meta:
        unique_together = ['user', 'project']

# 다른 부분(article, project 등등)은 model에 클래스 생성 이후 Form도 같이 만들어주나
# subscription의 경우 user에게 입력받아야할 값이 따로 없기 때문에 Form을 만들 필요 없음