from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer

class BookingCreateView(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        print("Request data:", request.data)  # Отладка: что приходит в запросе
        if serializer.is_valid():
            print("Validated data:", serializer.validated_data)  # Отладка: что валидировано
            booking = serializer.save()
            return Response({"booking_id": booking.id})
        print("Serializer errors:", serializer.errors)  # Отладка: ошибки валидации
        return Response({"error": serializer.errors}, status=400)

class BookingDeleteView(APIView):
    def delete(self, request, booking_id):
        try:
            booking = Booking.objects.get(id=booking_id)
            booking.delete()
            return Response({"message": "Booking deleted"})
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=404)

class BookingListView(APIView):
    def get(self, request):
        room_id = request.query_params.get("room_id")
        if not room_id:
            return Response({"error": "room_id is required"}, status=400)
            
        bookings = Booking.objects.filter(room_id=room_id).order_by("date_start")
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)