# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.PostListView.as_view(),
         name='bosh'),

    path('haqida/',
         views.HaqidaView.as_view(),
         name='haqida'),

    path('posts/<int:pk>/',
         views.PostDetailView.as_view(),
         name='post_detail'),

    path('posts/yangi/',
         views.PostCreateView.as_view(),
         name='post_create'),

    path('posts/<int:pk>/tahrir/',
         views.PostUpdateView.as_view(),
         name='post_update'),

    path('posts/<int:pk>/ochir/',
         views.PostDeleteView.as_view(),
         name='post_delete'),
]