DROP TABLE IF EXISTS artists CASCADE;
DROP TABLE IF EXISTS releases CASCADE;
DROP TABLE IF EXISTS reviews CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS artist_releases CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    song_name TEXT,
    rating INTEGER,
    comment TEXT,
    user_id INTEGER REFERENCES users ON DELETE CASCADE
);

CREATE TABLE releases (
    id SERIAL PRIMARY KEY,
    song TEXT,
    artist TEXT,
    album TEXT,
    year INTEGER,
    reviews INTEGER REFERENCES reviews ON DELETE CASCADE
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE artist_releases (
    artist_id INTEGER REFERENCES artists(id) ON DELETE CASCADE,
    release_id INTEGER REFERENCES releases(id) ON DELETE CASCADE,
    PRIMARY KEY (artist_id, release_id)
);
