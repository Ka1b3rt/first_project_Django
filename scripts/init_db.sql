CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    room_id INTEGER REFERENCES rooms(id) ON DELETE CASCADE,
    date_start DATE NOT NULL,
    date_end DATE NOT NULL,
    CHECK (date_start < date_end)
);

CREATE INDEX idx_bookings_room_id ON bookings(room_id);
CREATE INDEX idx_bookings_date_start ON bookings(date_start);