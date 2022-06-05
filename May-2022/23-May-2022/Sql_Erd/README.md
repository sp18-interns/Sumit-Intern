# Sumit-Intern

# Date 23-May-2022

## SQL-Handson for Create Table with Primary key & Foregin Key 
### SQL-Handson for ERD- Entity Relationship Diagram

- ✅ Query syntax for Create Table 
```
--Use your database
USE sumi;
GO

--1. Create 'SP18' table
CREATE TABLE SP18(
BranchID INT IDENTITY PRIMARY KEY, --auto-increment primary key
BranchPlace VARCHAR(30),
BranchState VARCHAR(10),
);

--2. Create 'Manager' table
CREATE TABLE Manager(
ManagerId INT PRIMARY KEY,
DeptName VARCHAR(10),
BranchId INT FOREIGN KEY REFERENCES dbo.SP18(BranchId),
);

--3. Create 'EMPLOYEE' table
CREATE TABLE EMPLOYEE(
EmpID INT PRIMARY KEY,
EmpName VARCHAR(20) NOT NULL,
ManagerId INT FOREIGN KEY REFERENCES dbo.Manager (ManagerId) NULL
);

--4. Create 'Department' table
CREATE TABLE Department(
DepartmentId INT NOT NULL,
EmpId INT REFERENCES EMPLOYEE(EmpId),
);


```
- ![Alt text](Query_PK_Creat-Table.PNG?raw="True")


### ER-Diagram

- ![Alt text](ERD.PNG?raw="True")


