from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    # print(dir(request))
    # return HttpResponse("<h1> hi , I am testing </h1>")

    return  render(request, "home.html", {})

def info_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    # print(request.POST)
    # print(request.COOKIES)
    # print(request.FILES)
    map = {
        "name" : "Harjot",
        "major" : "CS",
        "li":[11,"bs",77]
    }
    return render(request, "info.html", map)