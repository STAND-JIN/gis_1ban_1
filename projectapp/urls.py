from django.urls import path

from projectapp.views import ProjectCreateView

# 라우팅할 때 사용되는 경로 이름
app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),

]