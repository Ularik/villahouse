from . import views
from django.contrib import admin
from django.urls import path

# app_name = 'app'
urlpatterns = [
    path("index/", views.index, name='index'),
    path("house_list/", views.HouseListView.as_view(), name='house_list'),
    path('house_detail/<slug:slug>/', views.house_detail_view, name='house_detail'),
    path('house_update/<slug:slug>/', views.house_update_view, name='house_update'),
    path('house_delete/<slug:slug>/', views.house_delete, name='delete'),
    path('house_create/', views.house_create_view, name='house_create'),
]
