from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWolrd


app_name = 'accountapp'

def hello_world(request):
    if request.method == 'POST':

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWolrd()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWolrd.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': 'hello_world_list'})
