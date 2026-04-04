# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bosh_sahifa, name='bosh_sahifa'),
    path('haqida/', views.haqida, name='haqida'),

    # int - faqat butun son
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),

    # str - har qanday matn (bo'sh joy bo'lmasligi kerak)
    path('users/<str:username>/', views.foydalanuvchi, name='foydalanuvchi'),

    # slug - harflar, raqamlar, tire va pastki chiziqlarni o'z ichiga olishi mumkin
    path('maqola/<slug:slug>/', views.maqola, name='maqola'),


]