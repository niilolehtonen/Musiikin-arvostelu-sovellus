CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name TEXT,
    release_id INTEGER REFERENCES releases ON DELETE CASCADE
);

CREATE TABLE releases (
    id SERIAL PRIMARY KEY,
    song TEXT,
    artist TEXT,
    album TEXT,
    year INTEGER,
    reviews INTEGER REFERENCES reviews ON DELETE CASCADE
);


CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    rating INTEGER,
    comment TEXT,
    user_id INTEGER REFERENCES users ON DELETE CASCADE
);

