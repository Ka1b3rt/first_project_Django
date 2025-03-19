from django.urls import include, path
from django.http import JsonResponse

def not_found(request, exception):
    return JsonResponse({"error": "Not Found"}, status=404)

urlpatterns = [
    path('rooms/', include('hotel_booking.apps.rooms.urls')),
    path('bookings/', include('hotel_booking.apps.bookings.urls')),
]

handler404 = 'hotel_booking.urls.not_found' 