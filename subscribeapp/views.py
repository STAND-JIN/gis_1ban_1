from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get(self, request, *arge, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])

        # 구독 여부 확인
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        # 이미 구독했으면 구독정보 제거
        if subscription.exists():
            subscription.delete()
        # 구독하지 않았으면 user는 user, project는 project로 저장
        else:
            Subscription(user=user, project=project).save()
        return super().get(request, *arge, **kwargs)

    # get 요청 이후 어디로 이동할 것인지 설정
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': kwargs['project_pk']})

