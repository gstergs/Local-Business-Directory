# urls.py

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
    path('', PublicBusinessListView.as_view(), name='public_list'),  # List of businesses available to the public
    path('<int:pk>/', BusinessDetailView.as_view(), name='business_detail'),  # Detail view of a single business
    path('<int:pk>/submit-review/', SubmitReviewView.as_view(), name='submit_review'),  # View to submit a review for a business
    path('wishlist/', wishlist, name='wishlist'),  # View for the user's wishlist
    path('<int:business_id>/add-to-wishlist/', add_to_wishlist, name='add_to_wishlist'),  # Add a business to the user's wishlist
    path('<int:business_id>/remove-from-wishlist/', remove_from_wishlist, name='remove_from_wishlist'),  # Remove a business from the user's wishlist
    path('business-detail-ajax/', business_detail_ajax, name='business_detail_ajax'),  # AJAX endpoint for business details

    # Admin Views
    path('admin/', AdminBusinessListView.as_view(), name='admin_business_list'),  # List of businesses for admins
    path('admin/<int:pk>/', AdminBusinessDetailView.as_view(), name='admin_business_detail'),  # Detail view of a business for admins
    path('admin/create/', BusinessCreateView.as_view(), name='admin_business_create'),  # View to create a new business
    path('admin/<int:pk>/update/', BusinessUpdateView.as_view(), name='admin_business_update'),  # View to update an existing business
    path('admin/<int:pk>/delete/', BusinessDeleteView.as_view(), name='admin_business_delete'),  # View to delete a business

    # Power User Views
    path('power-user-dashboard/', PowerUserDashboardView.as_view(), name='power_user_dashboard'),  # Dashboard view for power users
]
