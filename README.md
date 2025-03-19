# first_project_Django

# Hotel Booking Service

## API Endpoints

### Rooms
- **POST /rooms/create/** - Create a new room
  - Request: `curl -X POST -d "description=Deluxe Room" -d "price_per_night=150.50" http://localhost:9000/rooms/create/`
  - Response: `{"room_id": 1}`

- **DELETE /rooms/delete/<room_id>/** - Delete a room
  - Request: `curl -X DELETE http://localhost:9000/rooms/delete/1/`
  - Response: `{"message": "Room deleted"}`

- **GET /rooms/list/** - List rooms
  - Request: `curl -X GET "http://localhost:9000/rooms/list/?sort_by=price&order=desc"`
  - Response: `[{"id": 1, "description": "Deluxe Room", "price_per_night": 150.50, "created_at": "2025-03-19T12:00:00Z"}, ...]`

### Bookings
- **POST /bookings/create/** - Create a booking
  - Request: `curl -X POST -d "room_id=1" -d "date_start=2025-04-01" -d "date_end=2025-04-05" http://localhost:9000/bookings/create/`
  - Response: `{"booking_id": 1}`

## Decisions
- Использован ON DELETE CASCADE для автоматического удаления броней при удалении номера.
- Добавлены индексы для ускорения запросов по room_id и date_start.
- Реализована проверка пересечения дат при создании брони.