CREATE TABLE car(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model VARCHAR(100) NOT NULL,
    data VARCHAR(100) NOT NULL,
    defect VARCHAR(100) NOT NULL
);

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    phone VARCHAR(100) NOT NULL
);