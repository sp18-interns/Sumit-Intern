###CREATING DATABASE

CREATE DATABASE SUMIT_DEMO;

###INTO DATABASE SUMIT_DEMO

###CREATING NEW TABLE BANK 
```
CREATE TABLE BANK
(
PERSONID INT,
FIRSTNAME VARCHAR(255),
LASTNAME VARCHAR(255),
ADDRESS VARCHAR(255),
CITY VARCHAR(255),
ADHAR NUMERIC(13)
);
```
DROP TABLE BANK;

SELECT * FROM BANK;

###INSERTING INTO BANK
```
INSERT INTO BANK
--(PERSONID, FIRSTNAME, LASTNAME, ADDRESS, CITY)
VALUES (1, 'NARENDR', 'MODI', 'AGNIPATH', 'DELHI',9630498482), 
(2, 'AMIT', 'SHA', 'VIJAYPATH', 'DELHI',9630498482),
(3,'NIRMALA','SITARAMAN','RAJPATH','DELHI',9630498482),
(4,'NIRMALA','SITARAMAN','RAJPATH','BOMBAY',9630498482),
(5, 'AMIT', 'SHARMA', 'VIJAYPATH', 'DELHI',9630498482),
(6, 'AMIT', 'SHA', 'AGNIPATH', 'DELHI',9630498482);
```
SELECT * FROM BANK;

SELECT TOP 1 FIRSTNAME, LASTNAME FROM BANK ; 

###ALTERTING TABLE BANK USING ADD/DROP
- Alter table to add column with default value
ALTER TABLE BANK
ADD NATIONALITY VARCHAR(255) DEFAULT 'INDIAN';  

- Another query for alter table to add default value to column 
ALTER TABLE BANK
ADD CONSTRAINT df_NATIONALITY
DEFAULT 'INDIAN' FOR NATIONALITY;


SELECT * FROM BANK;


ALTER TABLE BANK 
DROP COLUMN NATIONALITY;

SELECT * FROM BANK;

###SELECTING SPECIFIC COLUMNS

SELECT FIRSTNAME FROM BANK;

SELECT * FROM BANK WHERE CITY = 'DELHI';

SELECT FIRSTNAME, LASTNAME FROM BANK WHERE PERSONID = 1;

###UPDATING TABLE

UPDATE BANK SET CITY = 'INDORE';

UPDATE BANK SET CITY = 'PUNE' WHERE FIRSTNAME = 'AMIT'; 

SELECT * FROM BANK
