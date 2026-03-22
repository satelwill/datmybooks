
import sqlite3

conn = sqlite3.connect('datmybooks.db')
cursor = conn.cursor()

#Sélection-Projection
print("Quels sont les titres des livres de Fantasy ?")
cursor.execute("SELECT titre, anPub FROM LesLivres WHERE genre = 'fantasy';")
resultats_1 = cursor.fetchall()
for ligne in resultats_1:
    print(f" -> Titre: {ligne[0]} (Année: {ligne[1]})")


#Opérateur Ensembliste
print("ID des amis ayant emprunté le livre 106 ET le livre 114 :")
requete_2 = """
SELECT idAm FROM LesEmprunts WHERE idL = 106
INTERSECT
SELECT idAm FROM LesEmprunts WHERE idL = 114;
"""
cursor.execute(requete_2)
resultats_2 = cursor.fetchall()
for ligne in resultats_2:
    print(f" -> ID Ami: {ligne[0]}")


#Jointure-Agrégation
print("Nombre de livres par auteur :")
requete_3 = """
SELECT A.nom, COUNT(E.idL) as NombreDeLivres 
FROM LesAuteurs A 
JOIN EcritPar E ON A.idA = E.idA 
GROUP BY A.nom;
"""
cursor.execute(requete_3)
resultats_3 = cursor.fetchall()
for ligne in resultats_3:
    print(f" -> Auteur: {ligne[0]} | Nombre de livres: {ligne[1]}")


requete4 = """
    SELECT idL, titre 
    FROM LesLivres 
    WHERE idL NOT IN (
        SELECT idL 
        FROM LesEmprunts 
        WHERE dateRetour IS NULL
    );
"""
cursor.execute(requete4)
resultats = cursor.fetchall()

print("Voici les livres qui sont sur votre étagère :")
for ligne in resultats:
    print(f" Disponible : {ligne[1]}")


print("Qui emprunte un livre en ce moment ?")

requete5 = """
    SELECT LesAmis.prenom, LesAmis.nom, LesLivres.titre, LesEmprunts.dateEmprunt
    FROM LesEmprunts
    JOIN LesAmis ON LesEmprunts.idAm = LesAmis.idAm
    JOIN LesLivres ON LesEmprunts.idL = LesLivres.idL
    WHERE LesEmprunts.dateRetour IS NULL;
"""

cursor.execute(requete5)
resultats = cursor.fetchall()


print("Voici les amis qui ont vos livres en ce moment :")
for ligne in resultats:
    prenom = ligne[0]
    nom_famille = ligne[1]
    titre_livre = ligne[2]
    date_emprunt = ligne[3]
    print(f" -> {prenom} {nom_famille} a le livre '{titre_livre}' (emprunté le {date_emprunt})")
conn.close()

