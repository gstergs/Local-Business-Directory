from django.contrib import admin
from django.urls import path, include
from Local_business_directory.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('businesses/', include('businesses.urls', namespace='businesses')),
    path('admin_businesses/', include('businesses.admin_urls', namespace='admin_businesses')),
]
