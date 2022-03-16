from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.main, name='games'),
    path('<slug:game_slug>/', views.detail, name='detail'),
    path('add_comment/<slug:game_slug>/', views.add_comment, name='add_comment')
    # path('like/',views.likes_add, name='likes')
]
