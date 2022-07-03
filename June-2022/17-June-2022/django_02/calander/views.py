from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def march(request):
    return HttpResponse("Joined as Intern in SP18 & kick Started Programing Concepts with OOPS Also GIT")


def april(request):
    return HttpResponse("Started Python Hands-on")


def monthly(request, month):
    readme = None
    if month == 'march':
        readme = "Joined as Intern in SP18 & kick Started Programing Concepts with OOPS Also GIT"
    elif month == 'april':
        readme = "Started Python Hands-on"
    else:
        return HttpResponseNotFound ('Not available ')
    return HttpResponse(readme)
