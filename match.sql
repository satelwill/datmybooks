DROP TABLE IF EXISTS LeMatch;
DROP TABLE IF EXISTS Joueurs;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Statistiques;


CREATE TABLE LeMatch(
    id varchar(20),
    team varchar(20),
    tirs int,
    Tirs_cadrés int,
    Passes int,
    fautes int,
    rouge int, 
    J 
)

CREATE TABLE Joueurs(
    id int,
    prenom varchar(20),
    nom varchar(20),
    anNais int;
    CONSTRAINT PK_Jouers PRIMARY KEY(id)

);
INSERT INTO Joueurs VALUES(1, 'Senne', 'Lammens',)

CREATE TABLE Team(
    id int,
    team varchar(20),
    position varchar(20),
    num int,

)
INSERT INTO 

CREATE TABLE Statistiques(
    id int; 
)