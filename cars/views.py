from django.shortcuts import render, redirect

CARS_DATA = {
    "toyota": {
        "title": "Тойота",
        "brand": "Toyota",
        "description": "Надёжные и практичные автомобили с упором на долговечность и экономичность.",
        "models": [
            {"name": "Camry", "year": 2023, "price": "3 500 000 ₽"},
            {"name": "RAV4", "year": 2024, "price": "4 200 000 ₽"},
            {"name": "Corolla", "year": 2022, "price": "2 800 000 ₽"}
        ]
    },
    "honda": {
        "title": "Хонда",
        "brand": "Honda",
        "description": "Автомобили с акцентом на динамику, технологии и комфорт управления.",
        "models": [
            {"name": "Civic", "year": 2023, "price": "3 300 000 ₽"},
            {"name": "CR-V", "year": 2024, "price": "4 100 000 ₽"},
            {"name": "Accord", "year": 2022, "price": "3 700 000 ₽"}
        ]
    },
    "renault": {
        "title": "Рено",
        "brand": "Renault",
        "description": "Практичные городские и кроссоверные модели с хорошим соотношением цена/оснащение.",
        "models": [
            {"name": "Duster", "year": 2024, "price": "2 900 000 ₽"},
            {"name": "Kaptur", "year": 2023, "price": "3 100 000 ₽"},
            {"name": "Logan", "year": 2022, "price": "1 800 000 ₽"}
        ]
    }
}

def home(request):
    return render(request, "cars/home.html", {
        "title": "Главная",
        "page": "home"
    })

def car_brand(request, brand):
    if brand not in CARS_DATA:
        return redirect('home')
    data = CARS_DATA[brand]
    return render(request, "cars/brand.html", {
        "title": data["title"],
        "brand_slug": brand,
        "brand_name": data["brand"],
        "description": data["description"],
        "models": data["models"]
    })
