# import sqlite3
# from sqlite3 import Error


# def creer_connexion(db_file):
#     """ cree une connexion a la base de donnees SQLite
#         specifiee par db_file
#     :param db_file: fichier BD
#     :return: objet connexion ou None
#     Origin: testzoo.py 
#     """
#     try:
#         conn = sqlite3.connect(db_file)
# 		#On active les foreign keys
#         conn.execute("PRAGMA foreign_keys = 1")
#         return conn
#     except Error as e:
#         print(e)
 
#     return None

# def select_tous_Auteurs(conn):
#     """
#     :param conn: objet connexion
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM LesAuteurs")
 
#     rows = cur.fetchall()
 
#     for row in rows:
#         print(row)

# def main():
#     database="datmybooks.db"
#     conn=creer_connexion(database)
#     #select_tous_Auteurs(conn)
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM LesAuteurs")

# if __name__ == "__main__":
#     main()


import sqlite3

# 1. Connect to your database
# (Make sure the filename matches whatever you called your database in Python!)
conn = sqlite3.connect('datmybooks.db')
cursor = conn.cursor()

print("=== REQUÊTE 1 : Sélection-Projection ===")
print("Quels sont les titres des livres de Fantasy ?")
cursor.execute("SELECT titre, anPub FROM LesLivres WHERE genre = 'fantasy';")
resultats_1 = cursor.fetchall()
for ligne in resultats_1:
    print(f" -> Titre: {ligne[0]} (Année: {ligne[1]})")


print("\n=== REQUÊTE 2 : Opérateur Ensembliste ===")
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


print("\n=== REQUÊTE 3 : Jointure-Agrégation ===")
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


print("\n=== REQUÊTE UTILE 4 : Statistiques par Genre ===")
requete_stats_genre = """
    SELECT genre, COUNT(idL) as Total
    FROM LesLivres
    GROUP BY genre
    ORDER BY Total DESC;
"""
cursor.execute(requete_stats_genre)
for ligne in cursor.fetchall():
    print(f" Genre: {ligne[0]} -> {ligne[1]} livre(s)")
# Close the connection
conn.close()

