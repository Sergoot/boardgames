from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Game, Comment
from .forms import CommentForm
from django.forms import model_to_dict
from django.http import JsonResponse
import json


def main(request):
    latest_games = Game.objects.order_by('-pub_date')
    paginator = Paginator(latest_games, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'games/main.html', context)


def detail(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    games_rec = Game.objects.filter(category=game.category)[:3]
    comment = game.comment.filter(active=True)
    form = CommentForm()
    context = {'game': game, 'form': form, 'comment': comment, 'rec': games_rec}
    return render(request, 'games/detail.html', context)

@require_POST
def add_comment(request, game_slug):
    game = get_object_or_404(Game, slug=game_slug)
    form = CommentForm(data=request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post = game
        new_comment.user = request.user
        new_comment.save()
        return JsonResponse(
            {"text": new_comment.text, 'user': new_comment.user.username}, status=201)
    else:
        return JsonResponse(form.errors.as_data(), safe=False, status=200)



# def likes_add(request):


