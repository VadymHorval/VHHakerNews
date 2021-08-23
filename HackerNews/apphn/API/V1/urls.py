from django.urls import path
from .views import *


urlpatterns = [
    path ('new123/', ItemsView),
]