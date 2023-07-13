from django.urls import path
from .views import index
#здесь все ссылки нашего приложения

urlpatterns = [

    path('', index)


]