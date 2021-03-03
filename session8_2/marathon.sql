.mode column
PRAGMA foreign_keys = ON; -- activates foreign key features in sqlite. It is disabled by default

CREATE TABLE Runners(
    ID INTEGER PRIMARY KEY, 
    EMAIL VARCHAR(100), 
    PHONE INTEGER, 
    GENDER VARCHAR(100)
);

CREATE TABLE Runs (
    ID  INTEGER PRIMARY KEY, 
    RUN_NAME  VARCHAR(100),
    RUN_DESCRIPTION  VARCHAR(100), 
    RUN_DATE DATETIME
);

CREATE TABLE RunnersRuns (
    RUNNER_ID INTEGER,
    RUN_ID INTEGER, 
    MIN_TAKEN INTEGER,
    FOREIGN KEY (RUNNER_ID) REFERENCES Runners(ID),
    FOREIGN KEY (RUN_ID) REFERENCES Runs(ID)
);

CREATE TABLE Challenges (
    ID INTEGER PRIMARY KEY, 
    CH_DESCRIPTION  VARCHAR(100)
);

CREATE TABLE ChallengesRuns (
    CHALLENGE_ID INTEGER,
    RUN_ID INTEGER, 
    FOREIGN KEY (CHALLENGE_ID) REFERENCES Challenges(ID),
    FOREIGN KEY (RUN_ID) REFERENCES Runs(ID)
);

INSERT INTO Runners VALUES (1,"email@com", 20174567890, 'female');
INSERT INTO Runners VALUES (2,"email@com", 204356789, 'male');
INSERT INTO Runners VALUES (3,"email@com", 202345678916, 'female');
INSERT INTO Runners VALUES (4,"email@com", 2074567890, 'female');
INSERT INTO Runners VALUES (5,"email@com", 20134567890, 'male');
INSERT INTO Runners VALUES (6,"email@com", 26960, 'male');
INSERT INTO Runners VALUES (7,"email@com", 201512, 'female');
INSERT INTO Runners VALUES (8,"email@com", 085906, 'transgender');

INSERT INTO Runs VALUES (1,"The ruby marathon", "desc", '2017-10-01 10:00:00');
INSERT INTO Runs VALUES (2,"The bridge challenge",  "desc",'2017-11-01 10:00:00');
INSERT INTO Runs VALUES (3,"The sea to mountain sprint", "desc",'2017-12-01 10:00:00');
INSERT INTO Runs VALUES (4,"Flat and fast marathon", "desc",'2017-09-01 10:00:00');
INSERT INTO Runs VALUES (5,"The wine route stroll", "desc",'2017-08-01 10:00:00');

INSERT INTO RunnersRuns VALUES (1,2, 20);
INSERT INTO RunnersRuns VALUES (1,1, 12);
INSERT INTO RunnersRuns VALUES (1,3, 11);
INSERT INTO RunnersRuns VALUES (1,5, 18);
INSERT INTO RunnersRuns VALUES (1,4, 10);
INSERT INTO RunnersRuns VALUES (2,4, 10);
INSERT INTO RunnersRuns VALUES (3,5, 45);
INSERT INTO RunnersRuns VALUES (4,1, 45);
INSERT INTO RunnersRuns VALUES (4,5, 34);
INSERT INTO RunnersRuns VALUES (5,1, 23);
INSERT INTO RunnersRuns VALUES (6,2, 56);
INSERT INTO RunnersRuns VALUES (7,1, 24);
INSERT INTO RunnersRuns VALUES (8,5, 13);

INSERT INTO Challenges VALUES (1,"The marathon challenge");
INSERT INTO Challenges VALUES (2,"The terrain challenge");

INSERT INTO ChallengesRuns VALUES (2,2);
INSERT INTO ChallengesRuns VALUES (2,3);
INSERT INTO ChallengesRuns VALUES (2,1);

INSERT INTO ChallengesRuns VALUES (1,1);
INSERT INTO ChallengesRuns VALUES (1,4);


SELECT "Write a SQL query to find the top 3 fastest women runners for a given race."; 
SELECT "--";
SELECT Runners.ID, Runners.EMAIL, RunnersRuns.MIN_TAKEN, Runs.ID FROM Runners
    JOIN RunnersRuns on Runners.ID = RunnersRuns.RUNNER_ID
    JOIN Runs on Runs.ID = RunnersRuns.RUN_ID
    WHERE RunnersRuns.RUN_ID = 1 and Runners.gender = 'female'
    ORDER BY RunnersRuns.MIN_TAKEN
    LIMIT 3;
    

SELECT "Write a SQL query to find all the runners' email addresses that successfully finished the marathon challenge."; 
SELECT "--";
SELECT Runners.ID, Runners.EMAIL FROM Runners
    JOIN RunnersRuns ON Runners.ID = RunnersRuns.RUNNER_ID
    JOIN ChallengesRuns ON ChallengesRuns.RUN_ID = RunnersRuns.RUN_ID
    WHERE ChallengesRuns.CHALLENGE_ID = 1 ;
