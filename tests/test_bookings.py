import pytest
from rest_framework.test import APIClient
from hotel_booking.apps.rooms.models import Room
from hotel_booking.apps.bookings.models import Booking

@pytest.mark.django_db
def test_create_booking():
    room = Room.objects.create(description='Test Room', price_per_night=100.00)
    client = APIClient()
    response = client.post('/bookings/create/', {
        'room': room.id,
        'date_start': '2025-04-01',
        'date_end': '2025-04-05'
    })
    assert response.status_code == 200
    assert 'booking_id' in response.json()
    assert Booking.objects.count() == 1

@pytest.mark.django_db
def test_delete_booking():
    room = Room.objects.create(description='Test Room', price_per_night=100.00)
    booking = Booking.objects.create(room=room, date_start='2025-04-01', date_end='2025-04-05')
    client = APIClient()
    response = client.delete(f'/bookings/delete/{booking.id}/')
    assert response.status_code == 200
    assert Booking.objects.count() == 0

@pytest.mark.django_db
def test_list_bookings():
    room = Room.objects.create(description='Test Room', price_per_night=100.00)
    Booking.objects.create(room=room, date_start='2025-04-01', date_end='2025-04-05')
    Booking.objects.create(room=room, date_start='2025-03-01', date_end='2025-03-05')
    client = APIClient()
    response = client.get(f'/bookings/list/?room_id={room.id}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]['date_start'] == '2025-03-01'