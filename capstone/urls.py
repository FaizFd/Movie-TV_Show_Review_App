from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("category/<str:category>", views.category, name="category"),
    path("categoriess", views.categoriess, name="categoriess"),
    path("categorys/<str:categorys>", views.categorys, name="categorys"),
    path("categoryss/<str:categoryss>", views.categoryss, name="categoryss"),
    path("categoriesss", views.categoriesss, name="categoriesss"),
    path("create", views.create, name="create"),
    path("submit",views.submit,name="submit"),
    path("listings/<int:id>",views.listingpage,name="listingpage"),
    path("cmntsubmit/<int:listingid>",views.cmntsubmit,name="cmntsubmit"),
    path("addcart/<int:listingid>",views.addcart,name="addcart"),
    path("removecart/<int:listingid>",views.removecart,name="removecart"),
    path("cart/<str:username>",views.cartpage,name="cartpage"),
    path("corlosal", views.corlosal, name="corlosal"),
    path("test", views.test, name="test"),
    path("search", views.search, name="search"),
]
