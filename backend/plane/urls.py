from django.urls import path
from . import views

urlpatterns = [
    path('flights_previous/', views.FlightAndPreviousView.as_view()),
    path('flights/', views.FlightView.as_view()),
    path('previous/', views.HistoryView.as_view()),
    path('flights/<int:pk>/', views.FlightDetail.as_view()),
    path('previous/<int:pk>/', views.HistoryDetail.as_view()),
]
