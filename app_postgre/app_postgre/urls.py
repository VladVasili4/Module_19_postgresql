
from django.contrib import admin
from django.urls import path
from task555.views import user_profile_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_profile_list)
]
