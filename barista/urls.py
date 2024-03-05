from django.urls import path
from barista import views

urlpatterns = [
    path('barista/', views.BaristaList.as_view()),
    path('barista/<int:pk>/', views.BaristaDetail.as_view())
]