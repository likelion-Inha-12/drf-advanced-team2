from django.shortcuts import render

from django.http import HttpResponse


def assignment(request):
    return HttpResponse("assignment server ok!")