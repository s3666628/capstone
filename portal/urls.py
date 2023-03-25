from django.urls import path
from . import views

# if this finds empty string for example will call views.portal_home function

urlpatterns = [
    path("", views.portal_home, name="portal_home"),
    path("trends/", views.trends, name="trends"),
    path("top-ten/", views.top_ten, name="top_ten"),
    path("mapping", views.mapping, name="mapping"),
]
