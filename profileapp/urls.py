from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    # update는 create와 달리 기존에 있던 것을 수정하는 것이기 때문에 바꾸고자 하는 대상을 지정해줘야 함 --> <int:pk>
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]