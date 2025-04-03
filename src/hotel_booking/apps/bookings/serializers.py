from rest_framework import serializers
from .models import Booking

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["room_id", "date_start", "date_end"]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "room", "date_start", "date_end"]