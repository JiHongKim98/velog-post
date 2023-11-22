from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_index, name='LoginUrl'),
    path('logout/', views.logout_index, name='LogoutUrl'),
    path('join/', views.join_index, name='JoinUrl'),
]