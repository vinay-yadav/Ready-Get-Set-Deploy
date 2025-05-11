from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

PROJECT_NAME = getattr(settings, 'PROJECT_NAME', "Unset Project Views")


def hello_world(request):
    return render(request, 'hello-world.html', {
        "project_name": PROJECT_NAME,
    })


def healthz_view(request):
    return HttpResponse('OK')


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
