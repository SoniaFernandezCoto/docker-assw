CREATE TABLE IF NOT EXISTS sample_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT UNIQUE  
);

INSERT OR REPLACE INTO sample_table (data) VALUES ('Hola desde la base de datos');

