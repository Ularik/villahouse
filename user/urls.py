from . import views
from django.urls import path

# app_name = 'user'
urlpatterns = [
    path('register/', views.user_register_view, name='register'),
    path('login/', views.user_login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('profile/', views.user_profile_view, name='profile')
]