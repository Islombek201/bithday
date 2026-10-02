from django.shortcuts import render


def birthday_greeting(request):
    """Tug'ilgan kun tabrigi sahifasi"""
    # URL orqali ism berish mumkin: /?name=Ali&from=Sardor
    name = request.GET.get('name', "BUVAJON")
    from_name = request.GET.get('from', "Islombek")
    message = request.GET.get(
        'message',
        "Sizga uzoq umir va baxt,yaxshi sog'liq va iloyim 100 ga kiring! 🎂"
    )

    context = {
        'name': name,
        'message': message,
        'from_name': from_name,
    }
    return render(request, 'greeting/birthday.html', context)
