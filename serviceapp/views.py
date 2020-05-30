from rest_framework import generics
from .models import TruckSchedule
from .serializers import TruckScheduleSerializer

class TruckScheduleAPIView(generics.ListCreateAPIView):
    queryset = TruckSchedule.objects.all()
    serializer_class = TruckScheduleSerializer