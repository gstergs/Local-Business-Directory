# urls.py
from django.urls import path
from .views import (
    PublicBusinessListView, SubmitReviewView, BusinessDetailView, business_detail_ajax
)

app_name = 'businesses'

urlpatterns = [
    path('', PublicBusinessListView.as_view(), name='business_list'),
    path('<int:pk>/', BusinessDetailView.as_view(), name='business_detail'),
    path('<int:pk>/submit-review/', SubmitReviewView.as_view(), name='submit_review'),
    path('ajax/detail/', business_detail_ajax, name='business_detail_ajax'),
]
