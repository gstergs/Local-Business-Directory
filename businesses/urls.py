from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from businesses import views as business_views  # Import your business views if needed

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include the business URLs
    path('', business_views.BusinessListView.as_view(), name='business_list'),
    path('<int:pk>/', business_views.BusinessDetailView.as_view(), name='business_detail'),
    path('add/', business_views.BusinessCreateView.as_view(), name='business_add'),
    path('<int:pk>/edit/', business_views.BusinessUpdateView.as_view(), name='business_edit'),
    path('<int:pk>/delete/', business_views.BusinessDeleteView.as_view(), name='business_delete'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    
    # If you have other apps with their own URLs, include them here
    # path('other_app/', include('other_app.urls')),
]
