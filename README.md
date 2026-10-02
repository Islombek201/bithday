# 🎉 Tug'ilgan Kun Tabrigi Sayti (Django)

Do'stingizga chiroyli tug'ilgan kun tabrigi uchun Django sayti.

## Imkoniyatlar

- 🎂 Chiroyli animatsiyalar (confetti, balloonlar, shamlar, yulduzlar)
- 🎵 Fon musiqasi (tugma orqali yoqish/o'chirish)
- ✨ Gradient yozuvlar va silliq animatsiyalar
- 📱 Mobil qurilmalarga moslashgan (responsive)
- Backend (Django) + Frontend (HTML/CSS/JS)

## Qanday ishga tushirish

```bash
# Virtual environment (tavsiya etiladi)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Django o'rnatish
pip install django

# Loyihani ishga tushirish
python manage.py runserver
```

Brauzerda oching: **http://127.0.0.1:8000/**

## O'zgartirishlar

### 1. Do'stingiz ismini o'zgartirish

`greeting/views.py` faylida:

```python
context = {
    'name': "Ali",                    # ← Do'stingiz ismi
    'message': "Senga eng yaxshi tilaklarim bilan! ...",
    'from_name': "Sening do'sting",   # ← O'zingizning ismingiz
}
```

### 2. O'z musiqangizni qo'yish

1. MP3 faylni `static/audio/` papkasiga qo'ying (masalan `happy_birthday.mp3`)
2. `greeting/templates/greeting/birthday.html` da audio qismini o'zgartiring:

```html
<audio id="bgMusic" loop>
    <source src="{% static 'audio/happy_birthday.mp3' %}" type="audio/mpeg">
</audio>
```

Va template boshiga qo'shing:

```html
{% load static %}
```

### 3. Dizaynni o'zgartirish

Barcha CSS va JS `birthday.html` ichida. Ranglar, animatsiyalar, matnlarni bemalol o'zgartirishingiz mumkin.

## Loyiha tuzilishi

```
birthday_site/
├── manage.py
├── birthday_site/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── greeting/
│   ├── views.py
│   ├── urls.py
│   └── templates/greeting/birthday.html
├── static/
│   ├── css/
│   ├── js/
│   ├── audio/     ← musiqa fayllari shu yerga
│   └── images/
└── templates/
```

## Ishlatish

1. `python manage.py runserver`
2. Linkni do'stingizga yuboring
3. Sahifa ochilganda confetti va balloonlar chiqadi
4. "Musiqa" tugmasini bosib qo'shiqni yoqing
5. "Confetti" va "Sharlar" tugmalari bilan yana animatsiya qiling

**Tabriklar! 🎂🎉**
