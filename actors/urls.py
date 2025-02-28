from django.urls import path
from . import views

urlpatterns = [
    path('actors/',views.ActorsListCreateView.as_view(),name='actors_view'),
    path('actors/<int:pk>/',views.ActorsRetriveUpdateDestroyView.as_view(),name='actors_rud')
]