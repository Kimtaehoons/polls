from django.urls import path
from control import views
#네임 스페이스
app_name = 'control'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'), #register경로 만들고 view로 가보자
    path('counter/', views.counter, name='counter'),
    path('calc_even_odd/', views.calc_even_odd, name='calc_even_odd'),
]