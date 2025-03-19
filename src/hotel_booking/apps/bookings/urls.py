from django.urls import path
from .views import BookingCreateView, BookingDeleteView, BookingListView

urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='booking-create'),
    path('delete/<int:booking_id>/', BookingDeleteView.as_view(), name='booking-delete'),
    path('list/', BookingListView.as_view(), name='booking-list'),
]