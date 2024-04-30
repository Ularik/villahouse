from django.urls import path, include
from . import views


urlpatterns = [
    path('leads/', views.lead_list_view, name='lead_list'),
    path('delete/<int:pk>/', views.lead_delete_view, name='lead_delete'),
    path('storage_list/', views.storage_list_view, name='storage_list')
]