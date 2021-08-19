from django.urls import path

from subcribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subcribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe')
]