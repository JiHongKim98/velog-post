from django.urls import path

from . import views

urlpatterns = [
    path('', views.using_DB_test, name='using_DB'),
]