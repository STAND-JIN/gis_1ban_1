from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'projectapp/create.html'
    
    # 게시판 생성에 성공하게 되면 해당 게시판으로 연결
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        user = self.request.user
        project = self.object

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        # project 안에 있는 article만 가져와 article_list에 담기
        article_list = Article.objects.filter(project=self.object)
        return super().get_context_data(object_list=article_list,
                                        subscription=subscription,
                                        **kwargs)

class ProjectListView(ListView):
    model = Project
    # 프로젝트의 리스트를 담고 있어야 되기 때문에 다른 클래스와 달리 context_object_name이 'project_list'
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20