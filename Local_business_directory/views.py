# views.py

from django.shortcuts import render
from django.views import View
from businesses.models import Business, Review, Category

class HomeView(View):
    def get(self, request, *args, **kwargs):
        # Fetch featured businesses (top 5)
        featured_businesses = Business.objects.all()[:5]
        # Fetch latest reviews (sorted by creation date)
        latest_reviews = Review.objects.order_by('-created_at')[:5]
        # Fetch all categories
        categories = Category.objects.all()

        # Context data to be passed to the template
        context = {
            'featured_businesses': featured_businesses,
            'latest_reviews': latest_reviews,
            'categories': categories,
        }

        return render(request, 'home.html', context)  # Render the home template with context data
