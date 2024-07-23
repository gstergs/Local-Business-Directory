# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Local_business_directory.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface URL
    path('', HomeView.as_view(), name='home'),  # Home view URL
    path('accounts/', include('accounts.urls', namespace='accounts')),  # URLs for accounts app
    path('businesses/', include('businesses.urls', namespace='businesses')),  # URLs for businesses app
    path('admin_businesses/', include('businesses.admin_urls', namespace='admin_businesses')),  # Admin URLs for businesses
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
