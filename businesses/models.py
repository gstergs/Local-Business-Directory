# models.py

from django.db import models
from django.conf import settings

# Category model for categorizing businesses
class Category(models.Model):
    name = models.CharField(max_length=255)  # Name of the category
    description = models.TextField()  # Description of the category

    def __str__(self):
        return self.name  # String representation of the category

# Business model to store business information
class Business(models.Model):
    name = models.CharField(max_length=255)  # Name of the business
    description = models.TextField()  # Description of the business
    category = models.ForeignKey(Category, related_name='businesses', on_delete=models.CASCADE)  # Foreign key to Category
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Foreign key to the user who owns the business
    image = models.ImageField(upload_to='business_images/', blank=True, null=True)  # Image field for business images
    location = models.CharField(max_length=255, blank=True, null=True)  # New field for location of the business

    def __str__(self):
        return self.name  # String representation of the business

# Review model to store reviews for businesses
class Review(models.Model):
    business = models.ForeignKey(Business, related_name='reviews', on_delete=models.CASCADE)  # Foreign key to Business
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Foreign key to the user who wrote the review
    rating = models.IntegerField()  # Rating given in the review
    comment = models.TextField()  # Comment of the review
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the review was created

    def __str__(self):
        return f'{self.rating} by {self.user.username} for {self.business.name}'  # String representation of the review

# Wishlist model to manage user's wishlists
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Foreign key to the user who owns the wishlist
    businesses = models.ManyToManyField(Business, related_name='wishlists')  # Many-to-many relationship with Business

    def __str__(self):
        return f"{self.user.username}'s Wishlist"  # String representation of the wishlist
