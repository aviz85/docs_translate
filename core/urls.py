from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='document')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    # Add any additional core-specific URLs here
]
