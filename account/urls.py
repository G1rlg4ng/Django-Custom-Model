from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
]