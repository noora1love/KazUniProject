from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_home, name='login_main'),
    path('next', views.Next, name='next'),
    path('register', views.Register, name='register')

]
