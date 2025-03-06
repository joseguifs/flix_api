from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions

class ReviewListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    