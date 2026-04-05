create database HouseDb ;
go 
use HouseDb ;
go 

CREATE TABLE Houses (
    Id INT PRIMARY KEY IDENTITY(1,1),
    Area FLOAT,
    Bedrooms INT,
    Bathrooms INT,
    Floors INT,
    Location NVARCHAR(100),
    Price FLOAT
);

Insert into Houses(Area,Bedrooms,Bathrooms,Floors,Location,Price) Values 
(100,3,2,1,'HCM',2.5),
(150,3,2,2,'HCM',3.2),
(200,4,3,2,'HN',5.0),
(120,2,1,1,'DN',2.0),
(180,4,2,2,'HCM',4.2);