from django.urls import path 

from apps.shared import views 


urlpatterns = [
    path('region/list/', views.RegionListApiView.as_view(), name='region list api'),
]