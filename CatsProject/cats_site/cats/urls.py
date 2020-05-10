from django.urls import path

from . import views


urlpatterns=[
    path("", views.CatsView.as_view())
]

