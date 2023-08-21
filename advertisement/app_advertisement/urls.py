from django.urls import path

from .views import index, top_sellers, advertisementpost, register, login, profile


urlpatterns = [
    path("index.html", index, name="main-page"),
    path("top-sellers.html",top_sellers,name="top_sellers"),
    path("advertisement-post/", advertisementpost, name="post")
]