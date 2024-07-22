from django.urls import path
from .views import BusinessListView, BusinessDetailView, BusinessCreateView, BusinessUpdateView, BusinessDeleteView

urlpatterns = [
    path('', BusinessListView.as_view(), name='business_list'),
    path('<int:pk>/', BusinessDetailView.as_view(), name='business_detail'),
    path('add/', BusinessCreateView.as_view(), name='business_add'),
    path('<int:pk>/edit/', BusinessUpdateView.as_view(), name='business_edit'),
    path('<int:pk>/delete/', BusinessDeleteView.as_view(), name='business_delete'),
]
