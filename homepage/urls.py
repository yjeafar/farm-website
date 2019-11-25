from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('create-account/', views.createAccount, name="createAccont"),
    path('about-me/', views.aboutMe, name="aboutMe"),
    path('contact-me/', views.contactMe, name="contactMe"),
]
