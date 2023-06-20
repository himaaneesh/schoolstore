from . import views
from django.urls import path
from .views import login, register, confirm_order

urlpatterns = [

    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login, name='login'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('logout/',views.logout,name='logout'),

]

