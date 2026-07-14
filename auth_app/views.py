from django.shortcuts import render

# Учебные пользователи. В реальном проекте так НЕ хранят пароли!
USERS = {
    "admin": {"password": "admin123", "role": "Администратор"},
    "user": {"password": "user123", "role": "Пользователь"},
}

def login_view(request):
    message = ""
    greeting = ""
    role = ""

    if request.method == "POST":
        login = request.POST.get("login", "").strip()
        password = request.POST.get("password", "").strip()

        user_data = USERS.get(login)

        if user_data and user_data["password"] == password:
            greeting = f"Добро пожаловать, {login}!"
            role = user_data["role"]
        else:
            message = "Неверные логин или пароль."

    return render(request, "login.html", {
        "message": message,
        "greeting": greeting,
        "role": role,
    })
