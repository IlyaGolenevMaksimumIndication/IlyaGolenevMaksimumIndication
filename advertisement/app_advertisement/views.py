from django.http import HttpResponse
from django.http import render

def index(request):
    return render(request, "index.html")

def top_sellers(request):
    return render(request, "top-sellers.html")

def advertisementpost(request):
    return render(request, "advertisement-post.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")

def advertisement(request):
    return render(request, "advertisement.html")






