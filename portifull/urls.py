from django.urls import path
from . import views

urlpatterns = [
    path('', views.logon, name='logon'),
    path('sing/', views.sing, name='sing'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),  # Adicione esta linha
    ]