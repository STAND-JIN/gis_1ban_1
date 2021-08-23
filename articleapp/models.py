from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# SET_NULL = user가 삭제되어도 게시글은 작성자 미상으로 남음
# related_name은 나중에 유저와 연결할 때 사용되는 이름 ex) user.article
from projectapp.models import Project


class Article(models.Model):
    writer  = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True)
    #  null=True 는 제목없음 가능
    title   = models.CharField(max_length=200, null=True)
    image   = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)
    # 작성시간 입력
    # auto_now_add=True 는 게시글이 DB에 저장되는 시점을 기준으로 자동 입력
    # 따로 User에게 입력받거나 우리가 직접 입력해줄 수고로움을 덜 수 잇음
    created_at = models.DateField(auto_now_add=True)

    like = models.IntegerField(default=0)