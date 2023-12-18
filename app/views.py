from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from app.models import Games
class Something(ListView):
    model = Games
    template_name = "home.html"
    context_object_name = 'game_list'
class Gamedetailview(LoginRequiredMixin,DetailView):
    model=Games
    template_name='game_t.html'
    context_object_name ='game'