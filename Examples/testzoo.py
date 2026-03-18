

import sqlite3
from sqlite3 import Error
 
def creer_connexion(db_file):
    """ cree une connexion a la base de donnees SQLite
        specifiee par db_file
    :param db_file: fichier BD
    :return: objet connexion ou None
    """
    try:
        conn = sqlite3.connect(db_file)
		#On active les foreign keys
        conn.execute("PRAGMA foreign_keys = 1")
        return conn
    except Error as e:
        print(e)
 
    return None
 
 
def select_tous_animaux(conn):
    """
    :param conn: objet connexion
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM LesAnimaux")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def majBD(conn, file):

    # Lecture du fichier et placement des requetes dans un tableau
    createFile = open(file, 'r')
    createSql = createFile.read()
    createFile.close()
    sqlQueries = createSql.split(";")

    # Execution de toutes les requetes du tableau
    cursor = conn.cursor()
    for query in sqlQueries:
        cursor.execute(query)

        
def main():
    database = "zoo.db"

    # creer une connexion a la BD
    conn = creer_connexion(database)
    
    # remplir la BD 
    print("1. On cree LesAnimaux zoo et on les initialise avec des premieres valeurs.")
    majBD(conn, "zoo.sql")
    
    # lire la BD
    print("2. Liste de tous les animaux")
    select_tous_animaux(conn)
 

if __name__ == "__main__":
    main()
