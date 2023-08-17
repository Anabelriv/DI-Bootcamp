"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent.views import RentalAPIView, CustomerAPIView, VehicleAPIView, RentalStationAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/rental/', RentalAPIView.as_view(), name='rental-list'),
    path('rent/rental/<int:pk>/', RentalAPIView.as_view(), name='rental-detail'),
    path('rent/customer/', CustomerAPIView.as_view(), name='customer-list'),
    path('rent/customer/add/', CustomerAPIView.as_view(), name='customer-add'),
    path('rent/vehicle/', VehicleAPIView.as_view(), name='vehicle-list'),
    path('rent/vehicle/add/', VehicleAPIView.as_view(), name='vehicle-add'),
    path('rent/vehicle/<int:pk>/', VehicleAPIView.as_view(), name='vehicle-detail'),
    path('rent/station/', RentalStationAPIView.as_view(), name='station-list'),
    path('rent/station/add/', RentalStationAPIView.as_view(), {'action': 'add'}, name='station-add'),
    path('rent/station/<int:pk>/', RentalStationAPIView.as_view(), name='station-detail'),
    path('rent/station/distribution/', RentalStationAPIView.as_view(), {'action': 'distribution'}, name='station-distribution'),
    path('rent/station/distribute/', RentalStationAPIView.as_view(), {'action': 'distribute'}, name='station-distribute'),
]
