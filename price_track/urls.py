from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flipkart-tracker", views.price_tracker),
]
