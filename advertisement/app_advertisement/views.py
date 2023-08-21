from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import AdvertisementForm

def index(request):
    advertisements = advertisements.objects.all()
    context = {'advertisements': advertisements}
    return render(request, "app_advertisements/index.html", context=context)

def top_sellers(request):
    return render(request, "app_advertisements/top-sellers.html")

def advertisementpost(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
    if form.is_valid():
        form.save(commit=False)
        advertisement = form.save(commit=False)
        print(request.user)
        advertisement.user = request.user
        advertisement.save()
        url = reverse('main-page')
        return redirect(url)
    else:
        form = AdvertisementForm()

    form = AdvertisementForm()
    context = {"form": form}
    return render(request, "app_advertisements/advertisement-post.html")






def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")

def advertisement(request):
    return render(request, "advertisement.html")






