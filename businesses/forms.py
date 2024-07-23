# forms.py

from django import forms
from .models import Review, Business

# Form for submitting reviews
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            # Widget for the rating field with min and max values
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            # Widget for the comment field with a specific row height
            'comment': forms.Textarea(attrs={'rows': 3}),
        }

# Form for creating or updating business entries
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description', 'category', 'image', 'location']  # Include location field
