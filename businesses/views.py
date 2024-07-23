from django.db.models import Avg
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, render
from .models import Business, Review, Category
from .forms import ReviewForm

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
    template_name = 'businesses/business_detail.html'
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(business=self.object)
        context['average_rating'] = Review.objects.filter(business=self.object).aggregate(Avg('rating'))['rating__avg']
        return context

def business_detail_ajax(request):
    business_id = request.GET.get('id')
    business = get_object_or_404(Business, pk=business_id)
    reviews = business.reviews.all()
    context = {
        'business': business,
        'reviews': reviews,
    }
    return render(request, 'businesses/business_detail_public.html', context)

# --- Admin Views ---

class BusinessCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Business
    template_name = 'admin/business_form.html'
    fields = ['name', 'description', 'category', 'image']

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('admin_businesses:admin_business_detail', kwargs={'pk': self.object.pk})

class BusinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Business
    template_name = 'admin/business_form.html'
    fields = ['name', 'description', 'category', 'image']

    def test_func(self):
        return self.request.user.is_superuser and self.request.user == self.get_object().owner

    def get_success_url(self):
        return reverse('admin_businesses:admin_business_detail', kwargs={'pk': self.object.pk})

class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business
    template_name = 'admin/business_confirm_delete.html'
    success_url = reverse_lazy('admin_businesses:admin_business_list')

    def test_func(self):
        return self.request.user.is_superuser and self.request.user == self.get_object().owner

class SubmitReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'businesses/review_form.html'

    def get_success_url(self):
        return reverse('businesses:business_detail', kwargs={'pk': self.object.business.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.business = get_object_or_404(Business, pk=self.kwargs['pk'])
        return super().form_valid(form)

class AdminBusinessListView(UserPassesTestMixin, ListView):
    model = Business
    template_name = 'admin/business_list.html'
    context_object_name = 'businesses'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return Business.objects.all()

class AdminBusinessDetailView(UserPassesTestMixin, DetailView):
    model = Business
    template_name = 'admin/business_detail.html'
    context_object_name = 'business'

    def test_func(self):
        return self.request.user.is_superuser and self.request.user == self.get_object().owner

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        context['reviews'] = self.object.reviews.all()
        average_rating = self.object.reviews.aggregate(Avg('rating'))['rating__avg']
        context['average_rating'] = round(average_rating, 1) if average_rating else 0
        return context
