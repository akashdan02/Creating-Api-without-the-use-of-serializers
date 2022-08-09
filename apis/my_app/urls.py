from django.urls import path

from .views import Volunteer, VolunteerDetail

urlpatterns = [
    path('', Volunteer.as_view()),
    path('<int:pk>/', VolunteerDetail.as_view()),
]