from django.urls import path

from . import views

urlpatterns = [
    path('session', views.POST_index_session, name='using_session')
]