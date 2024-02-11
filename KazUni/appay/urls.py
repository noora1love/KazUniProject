from django.urls import path
from . import views
from .views import delete_selected,DataListView, ModelPaysAPIView, CountrypartyDetailView, DealDetailView

urlpatterns = [
    path('', views.appay_home, name='appay_main'),
    path('createform/', views.appay_createform, name='appay_createform'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='appay_form'),
    path('data/', views.NewsDetailView.as_view(), name='appay_countryparty'),
    path('delete_selected/', delete_selected, name='appay_delete_selected'),
    path('createform/<str:model_name>_data/', DataListView.as_view(), name='data-list'),
    path('profile/', views.profile, name='profile'),
    path('api/v1/modelpayslist', ModelPaysAPIView.as_view(), name=''),

    path('countryparty/<int:pk>/', CountrypartyDetailView.as_view(), name='countryparty_detail'),
    path('deal/<int:pk>/', DealDetailView.as_view(), name='deal_detail'),
    path('<int:record_id>/update/', views.get_model_pay_data, name='appay_update'),


    path('RegPay/', views.reg_pay_view, name='RegPay'),
    path('delete_selected_RegPay/', views.delete_selected_RegPay, name='RegPay_delete_selected'),
    path('RegPay/createform', views.reg_pay_createform, name='reg_pay_createform')
]


