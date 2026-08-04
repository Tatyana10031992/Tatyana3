import random
from django.shortcuts import render


POEMS_DATA = [
    {"title": "Одиночество звезд", "author": "А. Блок", "theme": "любовь", "text": "Звезды молчат в пустоте ледяной,\nВетер поет о разлуке ночной.\nСердце стучит, но ответа нет,\nТолько холодный, безмолвный свет."},
    {"title": "Город спит", "author": "С. Есенин", "theme": "жизнь", "text": "Улицы дремлют под лунным лучом,\nТени скользят за пустым крыльцом.\nГород затих, укрываясь во мгле,\nМысли мои растворились во сне."},
    {"title": "Крик моря", "author": "М. Цветаева", "theme": "творчество", "text": "Волна за волной набегает на берег,\nСтирая следы и разрушая мосты.\nЯ кричу в пустоту, но никто не ответит,\nЛишь эхо летит сквозь холодные сны."},
    {"title": "Осенний дождь", "author": "Ф. Тютчев", "theme": "природа", "text": "Дождь стучит по крышам монотонно,\nОсень красит мир в цвет темно-серый.\nЛистья падают тихо и беззвучно,\nЗавершая свой путь до последней меры."},
    {"title": "Надежда", "author": "А. Ахматова", "theme": "любовь", "text": "Сквозь годы и боль, сквозь разлуку и слезы,\nЯ верю, что счастье вернется ко мне.\nПусть гаснут огни и меняются грозы,\nНадежда живет в моем тихом огне."},
]

def fortune(request):
    predictions = [
        "Тебя ждет успех в новом проекте!",
        "Скоро ты встретишь старого друга.",
        "Будь осторожен с новыми предложениями.",
        "Твое упорство скоро окупится.",
        "Жди приятных новостей от семьи."
    ]
    return render(request, 'services/fortune.html', {'prediction': random.choice(predictions)})



def random_single(request):
    num = random.randint(1, 100)
    return render(request, 'services/random.html', {'number': num, 'type': 'одиночное число'})

def random_range(request, min_val, max_val):
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    num = random.randint(min_val, max_val)
    return render(request, 'services/random.html', {'number': num, 'type': f'число от {min_val} до {max_val}'})

def random_list(request, count):
    nums = [random.randint(1, 1000) for _ in range(count)]
    return render(request, 'services/random_list.html', {'numbers': nums, 'count': count})



def poem_random(request):
    poem = random.choice(POEMS_DATA)
    return render(request, 'services/poem.html', {'poem': poem, 'mode': 'random'})

def poem_by_author(request, author):
    filtered = [p for p in POEMS_DATA if p['author'].lower() == author.lower()]
    poem = random.choice(filtered) if filtered else None
    return render(request, 'services/poem.html', {'poem': poem, 'mode': f'автор: {author}', 'error': not filtered})

def poem_by_theme(request, theme):
    filtered = [p for p in POEMS_DATA if p['theme'].lower() == theme.lower()]
    poem = random.choice(filtered) if filtered else None
    return render(request, 'services/poem.html', {'poem': poem, 'mode': f'тема: {theme}', 'error': not filtered})



def list_authors(request):
    authors = sorted(list(set(p['author'] for p in POEMS_DATA)))
    return render(request, 'services/list.html', {'items': authors, 'title': 'Список авторов'})

def list_themes(request):
    themes = sorted(list(set(p['theme'] for p in POEMS_DATA)))
    return render(request, 'services/list.html', {'items': themes, 'title': 'Список тематик'})

def titles_by_theme(request, theme):
    titles = [p['title'] for p in POEMS_DATA if p['theme'].lower() == theme.lower()]
    return render(request, 'services/list.html', {'items': titles, 'title': f'Стихи по теме: {theme}'})

