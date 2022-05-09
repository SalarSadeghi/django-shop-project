from django.urls import path
from .views import HomePageView, HomeDetailView, CheckOutView
urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('detail/<int:pk>',HomeDetailView.as_view(),name='detail'),
    path('checkout/',CheckOutView.as_view(),name='checkout'),
]