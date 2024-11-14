-- relational databases are mathematically sound
-- logically coherent based on set theory
-- based on various research papers published by E. F. Codd at IBM labs in San Jose, CA

-- RElation, Attribute, Domain, Tuple, 
-- Keys: Super, primary, candidate, foreign key

SELECT 'Description: Show all TitanicData' AS Description;
SELECT * FROM TitanicData;
SELECT 'Survived Passengers (Name, Age, Fare)' AS Description;
SELECT Name, Age, Fare FROM TitanicData WHERE Survived = 1;
SELECT 'First-Class Passengers (Name, Sex, Age, Fare)' AS Description;
SELECT Name, Sex, Age, Fare FROM TitanicData WHERE Pclass = 1;