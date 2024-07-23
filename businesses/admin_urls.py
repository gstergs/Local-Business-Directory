# admin_urls.py
from django.urls import path
from .views import (
    AdminBusinessListView, AdminBusinessDetailView, BusinessCreateView, BusinessUpdateView, BusinessDeleteView
)

app_name = 'admin_businesses'

urlpatterns = [
    path('', AdminBusinessListView.as_view(), name='admin_business_list'),
    path('<int:pk>/', AdminBusinessDetailView.as_view(), name='admin_business_detail'),
    path('create/', BusinessCreateView.as_view(), name='admin_business_create'),
    path('<int:pk>/update/', BusinessUpdateView.as_view(), name='admin_business_update'),
    path('<int:pk>/delete/', BusinessDeleteView.as_view(), name='admin_business_delete'),
]
