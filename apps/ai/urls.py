from django.urls import path 

from apps.ai.views import DescribeYourSymptomsApiView, FindDoctorAndClinicForSymtomsApiView


urlpatterns = [
    path('descripbe_your_symptoms/', DescribeYourSymptomsApiView.as_view()),
    path('find_doctors_and_clinics/', FindDoctorAndClinicForSymtomsApiView.as_view()),
]