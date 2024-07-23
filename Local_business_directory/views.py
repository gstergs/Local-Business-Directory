from django.shortcuts import render
from django.views import View
from businesses.models import Business, Review, Category

class HomeView(View):
    def get(self, request, *args, **kwargs):
        featured_businesses = Business.objects.all()[:5]
        latest_reviews = Review.objects.order_by('-created_at')[:5]
        categories = Category.objects.all()

        context = {
            'featured_businesses': featured_businesses,
            'latest_reviews': latest_reviews,
            'categories': categories,
        }

        return render(request, 'home.html', context)
