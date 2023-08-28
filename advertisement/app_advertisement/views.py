from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import AdvertisementForm
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.urls import reverse_lazy

from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    title = request.GET.get("query")
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
        
   
    context = {'advertisements': advertisements, 'title': title}
    return render(request, "app_advertisements/index.html", context=context)

def top_sellers(request):
    users = users.objects.annotate(
        adv_count=Count("advertisement")
    ).order_by("-adv.count")
    context = {
        "users": users
    }
    return render(request, "app_advertisements/top-sellers.html", context=context)

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


def advertisement_view(request, pk):
    advertisement = Advertisement.objects.get(pk=pk)
    context = {
        "advertisement": advertisement
    }
    return render(request, "app_advertisements/advertisement.html", context=context)


def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")

def advertisement(request):
    return render(request, "advertisement.html")






# __lt=100 - меньше gt больше