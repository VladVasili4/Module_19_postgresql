from django.shortcuts import render
from .models import UserProfile

def user_profile_list(request):
    # Извлекаем все записи из модели UserProfile
    profiles = UserProfile.objects.all()
    # Передаем данные в шаблон
    return render(request, 'postgre_users.html', {'profiles': profiles})
