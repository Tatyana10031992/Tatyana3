from django.shortcuts import render

def calc_view(request):
    result = None
    error = None
    num1 = num2 = num3 = None

    if request.method == "POST":
        # Вариант с тремя отдельными полями
        raw1 = request.POST.get("num1", "").strip()
        raw2 = request.POST.get("num2", "").strip()
        raw3 = request.POST.get("num3", "").strip()
        operation = request.POST.get("operation")

        try:
            num1 = float(raw1)
            num2 = float(raw2)
            num3 = float(raw3)
        except ValueError:
            error = "Все три поля должны содержать корректные числа."
            return render(request, "calc.html", {
                "result": result,
                "error": error,
                "num1": num1,
                "num2": num2,
                "num3": num3,
            })

        if operation == "min":
            result = min(num1, num2, num3)
            op_name = "Минимум"
        elif operation == "max":
            result = max(num1, num2, num3)
            op_name = "Максимум"
        elif operation == "avg":
            result = (num1 + num2 + num3) / 3
            op_name = "Среднее арифметическое"
        else:
            error = "Не выбрана операция."

    return render(request, "calc.html", {
        "result": result,
        "error": error,
        "num1": num1,
        "num2": num2,
        "num3": num3,
    })
