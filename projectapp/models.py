from django.db import models

# Create your models here.

class Project(models.Model):
    # null은 form에서 빈칸 여부를 묻는 것이 아닌 DB에 할당되는 값의 유뮤임.
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False)
    # article이나 profile처럼 media 디렉터리에 project 디렉를 생성하고 하위에 저장
    image = models.ImageField(upload_to='project/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # 작성받을 요소들 입력이 끝났으면 migration 해주기
    # 입력받을 form을 생성. projectapp/form.py 생성

    # Project의 name을 string으로 출력
    # e.g. 새로운 Article을 create할 때 선택할 수 있는 게시판들의 이름 노출
    def __str__(self):
        return f'{self.name}'