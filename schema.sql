CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    name TEXT,
    artist TEXT
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    name TEXT,
    year INTEGER
);

CREATE TABLE reviews (
    song_name TEXT,
    rating INTEGER,
    comment TEXT,
    user_id INTEGER REFERENCES users,
    song_id INTEGER REFERENCES songs
);

