from django.urls import path

from .views import index, top_sellers, advertisementpost, register, login, profile


urlpatterns = [
    path("index.html", index, name="main-page")
    path("top-sellers.html",top-sellers,name="top_sellers")
    path("advertisement-post.html",advertisement-post,name="advertisement-post")
    path("register.html",register,name="register")
    path("login.html",login,name="login")
    path("profile.html",profile,name="profile")
    path("advertisement",advertisement,name="advertisement")
]