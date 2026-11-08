"""PLACEHOLDER views: the port of Sterr Agency's growth system replaces this file."""
from django.http import HttpResponse


def placeholder(request, *args, **kwargs):
    return HttpResponse("Coming soon", content_type="text/plain")
