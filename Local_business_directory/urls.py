from django.contrib import admin
from django.urls import path, include
from businesses import views as business_views

urlpatterns = [
    # Admin interface
    path('admin/', admin.site.urls),

    # Root URL configuration
    path('', business_views.BusinessListView.as_view(), name='home'),

    # Authentication URLs
    path('accounts/', include('accounts.urls')),

    # URLs for the 'businesses' app
    path('businesses/', include('businesses.urls')),
]
