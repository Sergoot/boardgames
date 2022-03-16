from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_view, name= 'logout'),
]