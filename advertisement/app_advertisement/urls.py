from django.urls import path

from .views import index, top_sellers, advertisementpost, advertisement_view

urlpatterns = [
    path("index.html", index, name="main-page"),
    path("top-sellers.html",top_sellers,name="top_sellers"),
    path("advertisement-post/", advertisementpost, name="post"),
    path("advertisement/<int:pk>", advertisement_view, name="adv"),
]