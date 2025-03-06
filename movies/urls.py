from django.urls import path
from . import views

urlpatterns = [
    path('movies/',views.MovieListCreateView.as_view(), name='movie_view'),
    path('movies/<int:pk>/', views.MoviesRetriveUpdateDestroyView.as_view(), name='movie_rud'),
    path('movies/stats', views.MoviesStats.as_view(), name='movies_stats'),
]