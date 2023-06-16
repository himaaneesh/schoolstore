from . import views
from django.urls import path
from .views import login, register, order_confirmation

urlpatterns = [

    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login, name='login'),
    path('newpage/',views.newpage,name='newpage'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('logout/',views.logout,name='logout'),

]

