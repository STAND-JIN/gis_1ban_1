from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('Hello_World/', hello_world, name='hello_world')
]
