from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from actors.models import Actors
from actors.serializers import ActorsSerializers
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalPermissions

class ActorsListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers

class ActorsRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalPermissions,)
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializers



