from django.shortcuts import render, redirect

HEADPHONES_DATA = {
    "budslive": {
        "name": "Samsung Galaxy Buds Live",
        "brand": "Samsung",
        "type": "внутриканальные, беспроводные",
        "features": [
            "активное шумоподавление",
            "влагозащита IPX2",
            "время работы до 6 часов",
            "сенсорное управление"
        ],
        "price": "14 990 ₽",
        "image": "buds_live.jpg"
    },
    "airpods": {
        "name": "Apple AirPods (3‑е поколение)",
        "brand": "Apple",
        "type": "вкладыши, беспроводные",
        "features": [
            "пространственное аудио",
            "защита от брызг и пота",
            "до 6 часов работы без кейса",
            "автоматическое переключение между устройствами Apple"
        ],
        "price": "18 990 ₽",
        "image": "airpods_3.jpg"
    },
    "wh1000xm5": {
        "name": "Sony WH‑1000XM5",
        "brand": "Sony",
        "type": "полноразмерные, беспроводные",
        "features": [
            "лучшее в классе шумоподавление",
            "30 часов автономной работы",
            "адаптивный контроль звука",
            "поддержка LDAC и 360 Reality Audio"
        ],
        "price": "39 990 ₽",
        "image": "wh1000xm5.jpg"
    }
}

def home(request):
    return render(request, "headphones/home.html")

def search_headphones(request):
    model_slug = request.GET.get('model', '').lower()

    if not model_slug:
      return redirect('home')

    if model_slug not in HEADPHONES_DATA:
      return redirect('home')

    data = HEADPHONES_DATA[model_slug]
    return render(request, "headphones/detail.html", {
        "title": data["name"],
        "name": data["name"],
        "brand": data["brand"],
        "type": data["type"],
        "features": data["features"],
        "price": data["price"],
        "image": data["image"],
    })