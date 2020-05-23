from django.urls import path

from . import views


urlpatterns=[
    path("", views.MainMenuView.as_view(), name="home"),
    path("coronavirus/", views.CoronaVirus.as_view(), name="corona"),
    path("contacts/", views.Contacts.as_view(), name="contacts"),
    path("test/", views.Test.as_view(), name="test"),
    path("_test/", views.finished_test, name="test_"),
    path("<slug:slug>/", views.middleware_view, name='middleware')
]

