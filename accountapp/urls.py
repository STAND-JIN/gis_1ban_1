from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    # .as_view()는 클래스를 함수로 뱉어주는 역할.
    path('create/', AccountCreateView.as_view(), name='create')
]