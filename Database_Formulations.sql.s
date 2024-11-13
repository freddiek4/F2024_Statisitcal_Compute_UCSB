-- relational databases are mathematically sound
-- logically coherent based on set theory
-- based on various research papers published by E. F. Codd at IBM labs in San Jose, CA

-- RElation, Attribute, Domain, Tuple, 
-- Keys: Super, primary, candidate, foreign key

CREATE DATABASE IF NOT EXISTS DemoDB;
USE DemoDB;

DROP TABLE IF EXISTS DataMatrix;

CREATE TABLE DataMatrix (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    value1 DECIMAL(10, 2),
    value2 DECIMAL(10, 2),
    value3 DECIMAL(10, 2),
    matrix_row JSON 
);

INSERT INTO DataMatrix (name, location, value1, value2, value3, matrix_row) 
VALUES 
    ('Alice', 'New York', 3.45, 2.56, 5.67, JSON_OBJECT('row1', 1, 'row2', 2)),
    ('Bob', 'San Francisco', 1.23, 4.56, 7.89, JSON_OBJECT('row1', 3, 'row2', 4)),
    ('Charlie', 'Los Angeles', 6.78, 9.01, 2.34, JSON_OBJECT('row1', 5, 'row2', 6));


SELECT 'Script executed successfully!' AS status_message;

SELECT * FROM DataMatrix;
SELECT name, location FROM DataMatrix WHERE value1 > 2;