CREATE TABLE guests (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT,
    email TEXT UNIQUE,
    passport_data TEXT,
    birth_date TEXT
);

CREATE TABLE rooms (
    id INTEGER PRIMARY KEY,
    room_number TEXT NOT NULL UNIQUE,
    category TEXT NOT NULL,
    capacity INTEGER NOT NULL,
    price_per_night REAL NOT NULL,
    status TEXT NOT NULL DEFAULT 'free'
        CHECK (status IN ('free', 'occupied', 'cleaning'))
);

CREATE TABLE bookings (
    id INTEGER PRIMARY KEY,
    guest_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    check_in_date TEXT NOT NULL,
    check_out_date TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'cancelled', 'completed')),
    FOREIGN KEY (guest_id) REFERENCES guests(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE stays (
    id INTEGER PRIMARY KEY,
    guest_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL,
    check_in_date TEXT NOT NULL,
    check_out_date TEXT,
    total_amount REAL,
    status TEXT NOT NULL DEFAULT 'active'
        CHECK (status IN ('active', 'completed')),
    FOREIGN KEY (guest_id) REFERENCES guests(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE payments (
    id INTEGER PRIMARY KEY,
    stay_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date TEXT NOT NULL,
    method TEXT,
    status TEXT NOT NULL DEFAULT 'pending'
        CHECK (status IN ('pending', 'completed', 'failed')),
    FOREIGN KEY (stay_id) REFERENCES stays(id)
);

CREATE TABLE additional_services (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE stay_services (
    stay_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    PRIMARY KEY (stay_id, service_id),
    FOREIGN KEY (stay_id) REFERENCES stays(id),
    FOREIGN KEY (service_id) REFERENCES additional_services(id)
);
