from django.urls import path
from contact_admin import views

urlpatterns = [
    path('contact_admin/', views.ContactList.as_view()),
    path('contact_admin/<int:pk>/', views.ContactDetail.as_view())
]
