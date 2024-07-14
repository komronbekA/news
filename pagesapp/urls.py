from django.urls import path
from .views import HomePageView, AboutPageView, KomronView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('komron/', KomronView.as_view(), name='komron'),
]