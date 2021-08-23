from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
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

@method_decorator(login_required, 'get')
# 구독중인 게시판의 게시글을 한번에 보기
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    # 구독중인 게시글만 볼 수 있게 필터링
    def get_queryset(self):
        # 유저가 구독한 게시판 중 'project'만 걸러내서 리스트로 만들어주기
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        article_list = Article.objects.filter(project__in=project_list)
        return article_list