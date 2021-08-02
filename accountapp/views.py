from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.functional import lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWolrd


app_name = 'accountapp'


@login_required
# (login_url=reverse_lazy('accountapp:login')) --> 커스텀 url을 사용하는 경우 url 직접 설정
# decorator는 메소드가 아닌 함수에 사용. 메소드는 다른 방법 사용.
def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWolrd()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        hello_world_list = HelloWolrd.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})

# CreateView를 상속받아 클래스 생성
class AccountCreateView(CreateView):
    # Django에서 기본적으로 제공하는 User model 사용
    model = User
    # User model을 만들 때 필요한 form 생성(내장클래스인 UserCreationForm 사용)
    form_class = UserCreationForm
    # 클래스와 함수의 호출방식이 다르기 때문에 reverse_lazy 사용.
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

    def get_success_url(self):
        # profile처럼 profile의 user가 필요한 것이 아니므로 곧바로 연결 가능
        # self.object == target.user
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    # 함수는 reverse, 클래스는 reverse_lazy 사용
    # success_url = reverse_lazy('accountapp:hello_world')
    # User에게 보게 될 html
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'
