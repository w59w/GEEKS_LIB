from django.contrib import admin
from django.urls import path
from main_page.views import home_page, about_me, about_my_pets, system_time

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),  # Главная страница
    path('about-me/', about_me),  # Страница "Обо мне"
    path('about-my-pets/', about_my_pets),  # Страница "Мой питомец"
    path('system-time/', system_time),  # Страница с системным временем
]
