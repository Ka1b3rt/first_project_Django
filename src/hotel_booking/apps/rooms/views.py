from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

class RoomCreateView(APIView):
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save()
            return Response({"room_id": room.id})
        return Response({"error": serializer.errors}, status=400)

class RoomDeleteView(APIView):
    def delete(self, request, room_id):
        try:
            room = Room.objects.get(id=room_id)
            room.delete()
            return Response({"message": "Room deleted"})
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=404)

class RoomListView(APIView):
    def get(self, request):
        sort_by = request.query_params.get("sort_by", "created_at")
        order = request.query_params.get("order", "asc")
        
        if sort_by not in ["price_per_night", "created_at"]:
            return Response({"error": "Invalid sort_by parameter"}, status=400)
        
        order_field = f"{'-' if order == 'desc' else ''}{sort_by}"
        rooms = Room.objects.all().order_by(order_field)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)