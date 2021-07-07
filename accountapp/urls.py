from django.urls import path

from accountapp.views import hello_world

urlpatterns = [
    path('Hello_World/', hello_world, name='hello_world')
]
