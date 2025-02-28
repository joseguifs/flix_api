from django.urls import path 
from . import views 

urlpatterns = [
    path('review/',views.ReviewListCreateView.as_view(),name='review_view'),
    path('review/<int:pk>', views.ReviewRetriveUpdateDestroyView.as_view(), name='review_rud')
]