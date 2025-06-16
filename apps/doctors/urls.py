from django.urls import path 

from apps.doctors import views

urlpatterns = [
    path('category/list/', views.DoctorCategoryListApiView.as_view(), name='doctor category list'),
    path('category/<uuid:category_id>/doctor/list/', views.DoctorListApiView.as_view(), name='doctor list api'),
    path('doctor/<uuid:id>/', views.DoctorDetailApiView.as_view(), name='doctor detail api'),
]