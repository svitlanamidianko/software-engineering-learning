

.mode column
.mode on

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INT,
    DateOrdered DATETIME,
    MonthOrdered INT
);

CREATE TABLE OrderItems (
    OrderID INT, --A unique integer to identify this account
    ProductID INT,
    Quantity INT
    PRIMARY KEY (OrderID, ProductID)
); 

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    Title TEXT,
    Description TEXT,
    Price NUMERIC(11, 2),
    Cost NUMERIC(11, 2)
);

INSERT INTO Products VALUES (1, "Widget", "Widge all your worries away!", 99.95, 32.00);
INSERT INTO Products VALUES (2, "Wodget", "Wodge all your worries away!", 199.95, 82.00);

INSERT INTO Orders VALUES (1, 1, "2025-01-01 10:00:00", 202501);
INSERT INTO OrderItems VALUES (1, 2, 1);
INSERT INTO OrderItems VALUES (1, 1, 2);
