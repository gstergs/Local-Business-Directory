from django.urls import path
from .views import (
    PublicBusinessListView, SubmitReviewView, BusinessDetailView,
    add_to_wishlist, remove_from_wishlist, wishlist,
    AdminBusinessListView, AdminBusinessDetailView, BusinessCreateView,
    BusinessUpdateView, BusinessDeleteView, PowerUserDashboardView,
    business_detail_ajax
)

app_name = 'businesses'

urlpatterns = [
    # Public Views
    path('', PublicBusinessListView.as_view(), name='public_list'),
    path('<int:pk>/', BusinessDetailView.as_view(), name='business_detail'),
    path('<int:pk>/submit-review/', SubmitReviewView.as_view(), name='submit_review'),
    path('wishlist/', wishlist, name='wishlist'),
    path('<int:business_id>/add-to-wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('<int:business_id>/remove-from-wishlist/', remove_from_wishlist, name='remove_from_wishlist'),
    path('business-detail-ajax/', business_detail_ajax, name='business_detail_ajax'),

    # Admin Views
    path('admin/', AdminBusinessListView.as_view(), name='admin_business_list'),
    path('admin/<int:pk>/', AdminBusinessDetailView.as_view(), name='admin_business_detail'),
    path('admin/create/', BusinessCreateView.as_view(), name='admin_business_create'),
    path('admin/<int:pk>/update/', BusinessUpdateView.as_view(), name='admin_business_update'),
    path('admin/<int:pk>/delete/', BusinessDeleteView.as_view(), name='admin_business_delete'),

    # Power User Views
    path('power-user-dashboard/', PowerUserDashboardView.as_view(), name='power_user_dashboard'),
]
