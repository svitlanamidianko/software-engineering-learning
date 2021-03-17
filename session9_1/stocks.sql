
CREATE TABLE TradingDesks(
    TradingDeskID INTEGER PRIMARY KEY,
    Name VARCHAR(50), 
    Description VARCHAR(50)
);
CREATE TABLE Companies(
    CompanySymbol VARCHAR(4) PRIMARY KEY,
    CompanyName VARCHAR(50)
);

CREATE TABLE DesksCompanies( -- shows which companies trading desk has
    TradingDeskID INTEGER,
    CompanySymbol VARCHAR(4),
    Quantity NUMERIC(4,3),
    FOREIGN KEY (TradingDeskID) REFERENCES TradingDesks(TradingDeskID),
    FOREIGN KEY (CompanySymbol) REFERENCES Companies(CompanySymbol)
);

CREATE TABLE Orders( -- shows what symbols certain desk has ordered
    OrderID int AUTO_INCREMENT PRIMARY KEY,
    TradingDeskID INTEGER,
    IsFilled BOOLEAN, 
    CompanySymbol VARCHAR(4),
    Quantity NUMERIC(4,3),
    OrderType VARCHAR(5),
    FOREIGN KEY (TradingDeskID) REFERENCES TradingDesks(TradingDeskID),
    FOREIGN KEY (CompanySymbol) REFERENCES Companies(CompanySymbol)
);

INSERT INTO TradingDesks VALUES (1, "name1", "desk1");
INSERT INTO TradingDesks VALUES (2, "name2", "desk2");
INSERT INTO TradingDesks VALUES (3, "name3", "desk3");
INSERT INTO TradingDesks VALUES (4, "name4", "desk4");

INSERT INTO Companies VALUES ('ABCD', "cname1");
INSERT INTO Companies VALUES ('ABDE', "cname2");
INSERT INTO Companies VALUES ('ABGH', "cname3");
INSERT INTO Companies VALUES ('AOOH', "cname4");

INSERT INTO DesksCompanies VALUES (1, 'ABCD', 2);
INSERT INTO DesksCompanies VALUES (1, 'ABDE', 4);
INSERT INTO DesksCompanies VALUES (1, 'AOOH', 1);
INSERT INTO DesksCompanies VALUES (2, 'ABCD', 2);
INSERT INTO DesksCompanies VALUES (3, 'ABGH', 6);
INSERT INTO DesksCompanies VALUES (4, 'ABGH', 7);


INSERT INTO Orders VALUES (1,2, TRUE , 'ABCD', 1, 'SELL');
INSERT INTO Orders VALUES (2, 1, FALSE , 'ABCD', 1, 'BUY');

/* Now write a transaction that updates the portfolios for both the selling company and the buying company. *\
SELECT * FROM Orders; 
BEGIN TRANSACTION;
INSERT INTO Orders VALUES (3,1, FALSE, 'ABCD',1, 'SELL'); 
INSERT INTO Orders VALUES (4, 2, FALSE,'ABCD',1, 'BUY'); 

UPDATE Orders SET IsFilled = True where  OrderID = 3;
UPDATE Orders SET IsFilled = True where  OrderID = 4;
END TRANSACTION;