from django.urls import path
from . import views

urlpatterns = [
    path('trips/create_trip', views.create_trip, name='create_trip'),
    path('trips/<int:trip_pk>/create', views.create_trip_day, name='create_trip_day'),
    path('trips/<int:pk>/delete_tripcomment/<int:comment_id>', views.comment_delete, name='delete_tripcomment'),
    path('trips/<int:pk>/delete', views.delete_trip, name='delete_trip'),
    path('trips/<int:pk>/tripdays/<int:day_pk>/delete', views.delete_trip_day, name='delete_trip_day'),
    path('trips/<int:pk>/edit', views.edit_trip, name='edit_trip'),
    path('trips/<int:pk>/tripdays/<int:day_pk>/edit', views.edit_trip_day, name='edit_trip_day'),
    path('trips/<int:trip_pk>/edit_tripcomment/<int:tc_pk>', views.comment_edit, name='edit_tripcomment'),
    path('trips/<int:pk>/follow', views.follow_trip, name='follow_trip'),
    path('trips/<int:pk>/tripdays/<int:day_pk>', views.trip_day, name='trip_day'),
    path('trips/<int:pk>/', views.trip_detail, name='tripdetail'),
    path('trips/traveller_planned', views.view_own_trips, name='owntriplist'),
    path('trips/', views.view_trips, name='triplist'),
]