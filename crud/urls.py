from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/list_view", views.list_view, name="list_view"),
    path("<id>/delete", views.delete_view, name="delete_view"),
]
