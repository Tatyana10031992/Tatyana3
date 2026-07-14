from django.shortcuts import render
from datetime import date, timedelta

def prog_day_view(request):
    result = None
    error = None
    year_input = ""

    if request.method == "POST":
        year_raw = request.POST.get("year", "").strip()
        year_input = year_raw

        try:
            year = int(year_raw)
            if year < 1 or year > 9999:
                error = "Год должен быть от 1 до 9999."
            else:
             
                start = date(year, 1, 1)
                prog_day = start + timedelta(days=255) 

                weekday_names = [
                    "понедельник", "вторник", "среда", "четверг",
                    "пятница", "суббота", "воскресенье"
                ]
                weekday = weekday_names[prog_day.weekday()]

                result = {
                    "date_str": prog_day.strftime("%d %B"),  
                    "weekday": weekday,
                    "year": year,
                }
        except ValueError:
            error = "Введите корректный год (число)."

    return render(request, "prog_day.html", {
        "result": result,
        "error": error,
        "year_input": year_input,
    })
