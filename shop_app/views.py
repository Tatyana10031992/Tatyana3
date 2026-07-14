from django.shortcuts import render

def register_view(request):
    data = None
    errors = []

    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        age_raw = request.POST.get("age", "").strip()
        email = request.POST.get("email", "").strip()
        gender = request.POST.get("gender")
        address = request.POST.get("address", "").strip()
        subscribe = request.POST.get("subscribe")  


        if not first_name:
            errors.append("Имя обязательно.")
        if not last_name:
            errors.append("Фамилия обязательна.")
        if not age_raw:
            errors.append("Возраст обязателен.")
        else:
            try:
                age = int(age_raw)
                if age < 0 or age > 150:
                    errors.append("Укажите корректный возраст (0–150).")
            except ValueError:
                errors.append("Возраст должен быть числом.")
                age = None

        if not email:
            errors.append("Email обязателен.")

        if not gender:
            errors.append("Выберите пол.")

        if not address:
            errors.append("Адрес обязателен.")

        if not errors:
            data = {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
                "email": email,
                "gender": gender,
                "address": address,
                "subscribe": subscribe is not None,
            }

    return render(request, "register.html", {
        "data": data,
        "errors": errors,
        "raw": request.POST if request.method == "POST" else {},
    })
