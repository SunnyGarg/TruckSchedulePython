from rest_framework import serializers

from .models import TruckSchedule

class TruckScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckSchedule
        fields = "__all__"