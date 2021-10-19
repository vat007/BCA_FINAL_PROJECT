from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('category/', views.category, name='category'),
    path('category/<str:pk>/', views.singleCategory, name='single-category'),
]
