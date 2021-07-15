from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 로그인을 할 수 있는 페이지의 url 생성.
    # Django 내장 클래스라서 호출 명령어만 알면 됨.
    # .as_view()는 클래스를 함수로 뱉어주는 역할.
    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
         name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    # pk = primary key
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update')
]