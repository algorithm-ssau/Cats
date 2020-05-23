from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import TypeOfWool
from .models import Cat
from .models import Characteristics

from django import views
from django.views import generic
from django.views.generic import View

from .cats_size_enum import dict_cats_styles

def middleware_view(request, slug):
    try:
        TypeOfWool.objects.get(url=slug)
        return WoolTypeDetailView.as_view()(request, slug)
    except Exception:
        Cat.objects.get(url=slug)
        return CatView.as_view()(request, slug)

class MainMenuView ( generic.View ):
    def get(self, request):
        wooltypes = TypeOfWool.objects.all()
        return render (request, "cats/index.html", {"wooltype_list": wooltypes})

class CoronaVirus ( generic.View ):
    def get(self, request):
        return render (request, "cats/coronavirus.html")

class Contacts ( generic.View ):
    def get(self, request):
        return render (request, "cats/contacts.html")

class Test ( generic.View ):
    def get(self, request):
        return render (request, "cats/test.html")

class WoolTypeDetailView( generic.View ):
    def get(self, request, slug):
        cats = Cat.objects.filter(type_of_wool__url=slug)
        wooltype = TypeOfWool.objects.get(url=slug).name
        return render (request, "cats/wool.html", {"cat_list": cats, "wool_type":wooltype})

class CatView ( generic.View ):
    def get(self, request, slug):
        cat = Cat.objects.get(url=slug)
        wooltype = TypeOfWool.objects.get(id=cat.type_of_wool_id)
        try:
            style = dict_cats_styles[slug]
        except Exception:
            style = 'photo'
        return render (request, "cats/cat.html", {"cat":cat, "wool_type":wooltype, "style":style})

def finished_test(request):
    life_style_id = request.POST["life_style_id"]
    care_id = request.POST["care_id"]
    attachment_id = request.POST["attachment_id"]
    activity_id = request.POST["activity_id"]
    noisiness_id = request.POST["noisiness_id"]
    sociability_id = request.POST["sociability_id"]

    perfect_cats = Characteristics.objects.filter(life_style_id=life_style_id, care_id=care_id, attachment_id=attachment_id, activity_id=activity_id, noisiness_id=noisiness_id, sociability_id=sociability_id)

    

    return HttpResponseRedirect("")