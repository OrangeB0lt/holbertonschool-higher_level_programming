-- creates database hbtn_0d_usa
-- fills the table with states on it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
       id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY(id)
       );
