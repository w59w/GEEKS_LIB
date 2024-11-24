from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home_page(request):
    return HttpResponse("""
        <h1>Добро пожаловать на мой сайт!</h1>
        <p>Выберите страницу:</p>
        <ul>
            <li><a href="/about-me/">Обо мне</a></li>
            <li><a href="/about-my-pets/">Мой питомец</a></li>
            <li><a href="/system-time/">Текущее время</a></li>
        </ul>
    """)



# View для информации о себе
def about_me(request):
    return HttpResponse("<h1>Привет! Меня зовут Кумушай. Я изучаю Python.</h1>")


# View для информации о питомце
def about_my_pets(request):
    pet_name = "Барсик"
    pet_image_url = "https://millenroadanimalhospital.com/wp-content/uploads/2019/03/Dogs.jpg"
    return HttpResponse(f"""
        <h1>Мой питомец</h1>
        <p>Имя: {pet_name}</p>
        <img src="{pet_image_url}" alt="{pet_name}" style="width:300px;">
    """)


# View для отображения системной даты и времени
def system_time(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"<h1>Текущее время: {current_time}</h1>")
