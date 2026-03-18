DROP TABLE IF EXISTS LesAuteurs;
DROP TABLE IF EXISTS LesLivres;
DROP TABLE IF EXISTS EcritPar;



CREATE TABLE LesAuteurs(
    idA int,
    nom varchar(20),
    prenom varchar(20),
    nationalite varchar(20),
    anNais int,
    CONSTRAINT PK_Auteurs PRIMARY KEY(idA)
);

INSERT INTO LesAuteurs VALUES (1,'Harari','Yaval','israélien',1976);
INSERT INTO LesAuteurs VALUES (2,'Levit','Stephen','américain',1967);
INSERT INTO LesAuteurs VALUES (3,'Kahneman','Daniel','américain',1934);
INSERT INTO LesAuteurs VALUES (4,'Gladwell','Malcolm','anglais',1963);
INSERT INTO LesAuteurs VALUES (5,'Grant','Adam','américain',1981);
INSERT INTO LesAuteurs VALUES (6,'Snow','Shane','américain',1981);
INSERT INTO LesAuteurs VALUES (7,'Barker','Eric','américain',1976);
INSERT INTO LesAuteurs VALUES (8,'Rowling','Joan','anglaise',1976);
INSERT INTO LesAuteurs VALUES (9,'MacHale','Donald','américain',1955);
INSERT INTO LesAuteurs VALUES (10,'Giran','Paul','français',1955);

CREATE TABLE LesLivres(
    idL int,
    titre varchar(50),
    genre varchar(20),
    anPub int,
    CONSTRAINT PK_livres PRIMARY KEY(idL)
);
INSERT INTO LesLivres VALUES (100, 'Pendragon: The Merchant of Death', 'Fantasy', 2002);
INSERT INTO LesLivres VALUES (101, 'Pendragon: The Lost City of Faar', 'Fantasy', 2003);
INSERT INTO LesLivres VALUES (102, 'Pendragon: The Never War', 'Fantasy', 2003);
INSERT INTO LesLivres VALUES (103, 'Pendragon: The Reality Bug', 'Fantasy', 2003);
INSERT INTO LesLivres VALUES (104,'Sapiens','Histoire',2011);
INSERT INTO LesLivres VALUES (105,'Homo Deus','Science',2015);
INSERT INTO LesLivres VALUES (106, 'Freakonomics', 'Économie', 2005);
INSERT INTO LesLivres VALUES (107, 'Think Like a Freak', 'Économie', 2014);
INSERT INTO LesLivres VALUES (108, 'Thinking, Fast and Slow', 'Psychologie', 2011);
INSERT INTO LesLivres VALUES (109, 'The Tipping Point', 'Sociologie', 2000);
INSERT INTO LesLivres VALUES (110, 'Outliers', 'Sociologie', 2008);
INSERT INTO LesLivres VALUES (111, 'Harry Potter à l''école des sorciers', 'Fantasy', 1997);
INSERT INTO LesLivres VALUES (112, 'Harry Potter et la Chambre des secrets', 'Fantasy', 1998);
INSERT INTO LesLivres VALUES (113, 'Harry Potter et le Prisonnier d''Azkaban', 'Fantasy', 1999);
INSERT INTO LesLivres VALUES (114, 'Think Again', 'Psychologie', 2021);
INSERT INTO LesLivres VALUES (115, 'Smartcuts', 'Business', 2014);
INSERT INTO LesLivres VALUES (116, 'Psychologie du peuple annamite', 'Sociologie', 1904);


CREATE TABLE EcritPar (
    idA int,
    idL int,
    CONSTRAINT PK_EcritPar PRIMARY KEY(idA, idL),
    CONSTRAINT FK_EcritPar_Auteurs FOREIGN KEY (idA) REFERENCES LesAuteurs(idA),
    CONSTRAINT FK_EcritPar_Livres FOREIGN KEY (idL) REFERENCES LesLivres(idL)
);

--D.J. MacHale
INSERT INTO EcritPar VALUES (9, 100);
INSERT INTO EcritPar VALUES (9, 101);
INSERT INTO EcritPar VALUES (9, 102);
INSERT INTO EcritPar VALUES (9, 103);

--  Yuval Harari 
INSERT INTO EcritPar VALUES (1, 104);
INSERT INTO EcritPar VALUES (1, 105);

--  Stephen Levit 
INSERT INTO EcritPar VALUES (2, 106);
INSERT INTO EcritPar VALUES (2, 107);

--  Daniel Kahneman 
INSERT INTO EcritPar VALUES (3, 108);

-- Malcolm Gladwell 
INSERT INTO EcritPar VALUES (4, 109);
INSERT INTO EcritPar VALUES (4, 110);

-- J.K. Rowling 
INSERT INTO EcritPar VALUES (8, 111);
INSERT INTO EcritPar VALUES (8, 112);
INSERT INTO EcritPar VALUES (8, 113);

--  Adam Grant (idA: 5)
INSERT INTO EcritPar VALUES (5, 114);

--  Shane Snow (idA: 6)
INSERT INTO EcritPar VALUES (6, 115);

-- Paul Giran (idA: 10)
INSERT INTO EcritPar VALUES (10, 116);