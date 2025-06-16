from django.urls import path

from apps.clinics import views 


urlpatterns = [
    path('category/list/', views.ClinicCategoryListApiView.as_view(), name='clinic category api'),
    path('category/<uuid:id>/clinic/list/', views.ClinicListApiView.as_view(), name='clinic list api'),
]