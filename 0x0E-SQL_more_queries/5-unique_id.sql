-- creates table unique_id when id has a default of 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
