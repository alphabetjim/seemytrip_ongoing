from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('travellers/', views.TravellerList, name = 'travellerlist'),
    path('travellerprofile/create_traveller/', views.create_traveller, name = 'create_traveller'),
    path('travellerprofile/delete_traveller/', views.delete_traveller, name = 'delete_traveller'),
    path('travellerprofile/edit_traveller/', views.edit_traveller, name = 'edit_traveller'),
    path('travellerprofile/view_profile/<int:pk>', views.traveller_profile, name = 'travellerprofile'),
    path('travellerprofile/view_profile/', views.view_profile, name = 'view_traveller'),
]