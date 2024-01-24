from django.urls import path

from . import views

urlpatterns = [
    path("mission/", views.mission, name="mission"),
    path("mission/<int:mission_id>/", views.mission, name="mission"),
]