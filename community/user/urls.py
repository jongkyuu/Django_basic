from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.regitster),
    path('login/', views.login),
    path('logout/', views.logout)
]
