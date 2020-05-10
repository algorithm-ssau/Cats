from django.shortcuts import render

from .models import Cat

from django import views
from django.views import generic
from django.views.generic import View

class CatsView ( generic.View ):
    def get(self, request):
        cats = Cat.objects.all()
        return render (request,"cats/cat_list.html", {"cat_list":cats})