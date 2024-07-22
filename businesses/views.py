from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST

from .models import Business, Review, Category
from .forms import ReviewForm

def home(request):
    return render(request, 'home.html')

class BusinessListView(generic.ListView):
    model = Business
    template_name = 'businesses/business_list.html'
    context_object_name = 'businesses'

class BusinessDetailView(generic.DetailView):
    model = Business
    template_name = 'businesses/business_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        similar_businesses = Business.objects.filter(category=self.object.category).exclude(id=self.object.id)
        context['similar_businesses'] = similar_businesses
        return context

class BusinessCreateView(LoginRequiredMixin, generic.CreateView):
    model = Business
    fields = ['name', 'description', 'category', 'image']
    template_name = 'admin/business_form.html'  # Updated path to 'admin'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BusinessUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Business
    fields = ['name', 'description', 'category', 'image']
    template_name = 'admin/business_form.html'  # Updated path to 'admin'

    def test_func(self):
        business = self.get_object()
        return self.request.user == business.owner or self.request.user.is_superuser

class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Business
    success_url = '/'
    template_name = 'admin/business_confirm_delete.html'  # Updated path to 'admin'

    def test_func(self):
        business = self.get_object()
        return self.request.user == business.owner or self.request.user.is_superuser

@method_decorator(require_POST, name='dispatch')
class SubmitRatingView(LoginRequiredMixin, generic.View):
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.business_id = self.kwargs['pk']
            review.save()
            return JsonResponse({'success': True, 'rating': review.rating})
        return JsonResponse({'success': False})
