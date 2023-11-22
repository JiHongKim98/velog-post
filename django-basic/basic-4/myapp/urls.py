from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>/<str:li_text>', views.index, name='index'),
    # URL : http://localhost:8000/myapp
    # URL 패턴명 : 'post_method'
    path('', views.POST_index, name='post_method'),
    path('cookie', views.POST_index_cookies, name='using_cookies'),
]