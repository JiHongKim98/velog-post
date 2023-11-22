from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>/<str:li_text>', views.index, name='index'),
]