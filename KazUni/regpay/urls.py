from django.urls import path
from . import views

urlpatterns = [
    path('', views.regpay_home, name='regpay_main'),
    path('createform/', views.regpay_createform, name='regpay_createform'),
    path('form/', views.regpay_form, name='regpay_form')
]
