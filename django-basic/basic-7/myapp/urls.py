from django.urls import path

from . import views

urlpatterns = [
    path('', views.using_DB_index, name='using_DB'),
]