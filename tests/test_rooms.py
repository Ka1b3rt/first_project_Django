import pytest
from rest_framework.test import APIClient
from hotel_booking.apps.rooms.models import Room

@pytest.mark.django_db
def test_create_room():
    client = APIClient()
    response = client.post('/rooms/create/', {'description': 'Test Room', 'price_per_night': 100.00})
    assert response.status_code == 200
    assert 'room_id' in response.json()
    assert Room.objects.count() == 1

@pytest.mark.django_db
def test_delete_room():
    room = Room.objects.create(description='Test Room', price_per_night=100.00)
    client = APIClient()
    response = client.delete(f'/rooms/delete/{room.id}/')
    assert response.status_code == 200
    assert Room.objects.count() == 0

@pytest.mark.django_db
def test_list_rooms():
    Room.objects.create(description='Cheap Room', price_per_night=50.00)
    Room.objects.create(description='Expensive Room', price_per_night=150.00)
    client = APIClient()
    response = client.get('/rooms/list/?sort_by=price_per_night&order=asc')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]['price_per_night'] == '50.00'