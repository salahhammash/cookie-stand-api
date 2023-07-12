from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Game


class GameListView(LoginRequiredMixin, ListView):
    template_name = "gamee/Game_list.html"
    model = Game
    context_object_name = "gamee"


class GameDetailView(LoginRequiredMixin, DetailView):
    template_name = "gamee/Game_detail.html"
    model = Game


class GameUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "gamee/Game_update.html"
    model = Game
    fields = "__all__"


class GameCreateView(LoginRequiredMixin, CreateView):
    template_name = "gamee/Game_create.html"
    model = Game
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class GameDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "gamee/Game_delete.html"
    model = Game
    success_url = reverse_lazy("Game_list")
