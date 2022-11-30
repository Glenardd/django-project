from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from baseball.models import Position, Person, Club, Play, Match

class HomePageView(ListView):
    model = Play
    context_object_name = 'play'
    template_name = "landingpage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClubView(ListView):
    model = Club
    context_object_name = 'club.html'
    template_name = "club.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_text'] = 'List of Teams'
        return context
    
    def get_queryset(self, *args,**kwargs):
        qs = super(ClubView, self).get_queryset(*args,**kwargs)
        return qs

class PlayView(ListView):
    model = Play
    context_object_name = 'player.html'
    template_name = "player.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, *args,**kwargs):
        qs = super(PlayView, self).get_queryset(*args,**kwargs)
        return qs