# forms.py

from django import forms
from .models import Review, Business

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'category', 'image', 'location']  # Include location field
