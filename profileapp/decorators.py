from django.http import HttpResponseForbidden
from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # 여기서 pk는 urls.py 에서 받는 <int:pk>와 동일.
        target_profile = Profile.objects.get(pk=kwargs['pk'])
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated