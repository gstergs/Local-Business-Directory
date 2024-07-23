from django.db.models import Avg
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Business, Review, Category, Wishlist
from .forms import ReviewForm
from .mixins import PowerUserMixin

# --- Public Views ---

class PublicBusinessListView(ListView):
    model = Business
    template_name = 'businesses/business_public_list.html'
    context_object_name = 'businesses'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('search')
        category_id = self.request.GET.get('category')

        if search_term:
            queryset = queryset.filter(name__icontains=search_term)
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class BusinessDetailView(DetailView):
    model = Business
    template_name = 'businesses/business_detail_public.html'
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(business=self.object)
        context['average_rating'] = Review.objects.filter(business=self.object).aggregate(Avg('rating'))['rating__avg']
        context['review_form'] = ReviewForm()
        return context

def business_detail_ajax(request):
    if request.method == 'GET':
        business_id = request.GET.get('id')
        try:
            business = Business.objects.get(id=business_id)
            data = {
                'name': business.name,
                'description': business.description,
                'image_url': business.image.url if business.image else None,
                # Add other business fields as needed
            }
            return JsonResponse(data)
        except Business.DoesNotExist:
            return JsonResponse({'error': 'Business not found'}, status=404)

# --- Wishlist Views ---

@login_required
def add_to_wishlist(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.businesses.add(business)
    return redirect('businesses:business_detail', pk=business_id)

@login_required
def remove_from_wishlist(request, business_id):
    business = get_object_or_404(Business, id=business_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.businesses.remove(business)
    return redirect('businesses:wishlist')

@login_required
def wishlist(request):
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    context = {
        'businesses': wishlist.businesses.all()
    }
    return render(request, 'businesses/wishlist.html', context)

# --- Review Submission View ---

class SubmitReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'businesses/submit_review.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.business = get_object_or_404(Business, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('businesses:business_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business'] = get_object_or_404(Business, pk=self.kwargs['pk'])
        return context

# --- Admin Views ---

class BusinessCreateView(LoginRequiredMixin, PowerUserMixin, CreateView):
    model = Business
    template_name = 'admin/add_business.html'
    fields = ['name', 'description', 'category', 'image', 'location']  # Added location field

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('businesses:power_user_dashboard')

class BusinessUpdateView(LoginRequiredMixin, PowerUserMixin, UpdateView):
    model = Business
    template_name = 'admin/business_form.html'
    fields = ['name', 'description', 'category', 'image', 'location']  # Added location field

    def get_success_url(self):
        return reverse('businesses:admin_business_detail', kwargs={'pk': self.object.pk})

class BusinessDeleteView(LoginRequiredMixin, PowerUserMixin, DeleteView):
    model = Business
    template_name = 'admin/business_confirm_delete.html'
    success_url = reverse_lazy('businesses:admin_business_list')

class AdminBusinessListView(PowerUserMixin, ListView):
    model = Business
    template_name = 'admin/business_list.html'
    context_object_name = 'businesses'
    paginate_by = 10

    def get_queryset(self):
        return Business.objects.all()

class AdminBusinessDetailView(PowerUserMixin, DetailView):
    model = Business
    template_name = 'admin/business_detail.html'
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        context['reviews'] = self.object.reviews.all()
        average_rating = self.object.reviews.aggregate(Avg('rating'))['rating__avg']
        context['average_rating'] = round(average_rating, 1) if average_rating else 0
        return context

class PowerUserDashboardView(LoginRequiredMixin, PowerUserMixin, ListView):
    model = Business
    template_name = 'businesses/power_user_dashboard.html'
    context_object_name = 'businesses'

    def get_queryset(self):
        return Business.objects.filter(owner=self.request.user)
