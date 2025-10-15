from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('sobre-mim/', views.sobre_mim, name='sobre_mim'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('buscar/', views.buscar, name='buscar'),
]
