from django.shortcuts import render
from datetime import datetime


DAY_INFO = {
    0: {"name": "Понедельник", "class": "monday", "img": "monday.jpg"},
    1: {"name": "Вторник", "class": "tuesday", "img": "tuesday.jpg"},
    2: {"name": "Среда", "class": "wednesday", "img": "wednesday.jpg"},
    3: {"name": "Четверг", "class": "thursday", "img": "thursday.jpg"},
    4: {"name": "Пятница", "class": "friday", "img": "friday.jpg"},
    5: {"name": "Суббота", "class": "saturday", "img": "saturday.jpg"},
    6: {"name": "Воскресенье", "class": "sunday", "img": "sunday.jpg"},
}

def current_day(request):
    today = datetime.now()
    weekday_num = today.weekday()  
    info = DAY_INFO[weekday_num]

    context = {
        "day_name": info["name"],
        "css_class": info["class"],
        "img_name": info["img"],
    }
    return render(request, "weekday/day.html", context)
