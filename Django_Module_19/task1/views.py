from django.shortcuts import render
from .models import Buyer, Game
from .forms import UserRegister


# Create your views here.
def main_page(request):
    return render(request, 'main_page.html')


def switch_games(request):
    title = 'Игры Nintendo'
    games = [game for game in Game.objects.all()]
    context = {
        'title': title,
        'games': games
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    text = 'Извините, Ваша корзина пуста'
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'shopping_cart.html', context)


def registration(request):
    usernames = [buyer.name for buyer in Buyer.objects.all()]
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = int(request.POST.get('age'))

        if username in usernames:
            info['error'] = "Пользователь уже существует"
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password == repeat_password and username not in usernames:
            Buyer.objects.create(name=username, balance=5000, age=age)
            info['message'] = f'Приветствуем, {username}!'
    return render(request, 'registration_page.html', context=info)
