

# Rapport de Mini-Projet : Base de Données de Bibliothèque Personnelle

## 1. Schéma de la Base de Données
Pour ce projet, la base de données a été conçue pour gérer une bibliothèque personnelle et les emprunts effectués par des amis. Elle dépasse le minimum requis de 3 tables en définissant 3 entités et 2 associations, offrant ainsi un modèle relationnel robuste.
**Les Entités :**
* **`LesAuteurs`** : Représente les écrivains.
    * Attributs : `idA` (Clé Primaire), `nom`, `prenom`, `nationalite`, `anNais`.
* **`LesLivres`** : Représente les ouvrages physiques dans la bibliothèque.
    * Attributs : `idL` (Clé Primaire), `titre`, `genre`, `anPub`.
* **`LesAmis`** : Représente les personnes pouvant emprunter des livres.
    * Attributs : `idAm` (Clé Primaire), `nom`, `prenom`, `nationalite`, `email`, `anNais`.

**Les Associations :**
* **`EcritPar`** : Relie les auteurs aux livres (gestion des co-auteurs possible).
    * Attributs : `idA` (Clé Étrangère), `idL` (Clé Étrangère).
    * Clé Primaire : (`idA`, `idL`).
* **`LesEmprunts`** : Relie les livres aux amis avec un suivi temporel.
    * Attributs : `idL` (Clé Étrangère), `idAm` (Clé Étrangère), `dateEmprunt`, `dateRetour`.
    * Clé Primaire : (`idL`, `idAm`, `dateEmprunt`).

---

## 2. Schéma de Relations et Contraintes

Pour modéliser cette application, nous avons défini le modèle relationnel donné ci-dessous. Comme dans le cours, les identifiants (clés primaires) des relations sont les attributs notés en caractères soulignés :

### Schéma des Relations
* **LesAuteurs** (<u>idA</u>, nom, prenom, nationalite, anNais)
* **LesLivres** (<u>idL</u>, titre, genre, anPub)
* **LesAmis** (<u>idAm</u>, nom, prenom, nationalite, email, anNais)
* **EcritPar** (<u>idA</u>, <u>idL</u>)
* **LesEmprunts** (<u>idL</u>, <u>idAm</u>, <u>dateEmprunt</u>, dateRetour)

### Contraintes d'intégrité référentielles
Pour garantir la cohérence des données (Foreign Keys), les contraintes suivantes sont appliquées :
* $EcritPar[idA] \subseteq LesAuteurs[idA]$
* $EcritPar[idL] \subseteq LesLivres[idL]$
* $LesEmprunts[idL] \subseteq LesLivres[idL]$
* $LesEmprunts[idAm] \subseteq LesAmis[idAm]$

---
## 3. Interrogation de la Base de Données (Requêtes)
Conformément aux consignes demandant une requête par niveau, voici les requêtes implémentées via Python.

### Niveau 1 : Sélection - Projection
*  Quels sont les titres et les années de publication de tous les livres appartenant au genre 'fantasy' ?
* **Algèbre relationnelle :** $$\pi_{titre, anPub}(\sigma_{genre='fantasy'}(LesLivres))$$
* **Code SQL :** 
```sql
SELECT titre, anPub FROM LesLivres WHERE genre = 'fantasy';
```

### Niveau 2 : Opérateurs Ensemblistes (Intersection)
* Quels sont les identifiants des amis ayant emprunté à la fois le livre numéro 106 (Freakonomics) ET le livre numéro 114 (Think Again) ?
* **Algèbre relationnelle :** $$\pi_{idAm}(\sigma_{idL=106}(LesEmprunts)) \cap \pi_{idAm}(\sigma_{idL=114}(LesEmprunts))$$
* **Code SQL :**
```sql
SELECT idAm FROM LesEmprunts WHERE idL = 106
INTERSECT
SELECT idAm FROM LesEmprunts WHERE idL = 114;
```

### Niveau 3 : Jointure - Agrégation
*  Quel est le nombre total de livres rédigés par chaque auteur présent dans la base de données ?
* **Algèbre relationnelle :** $$_{nom} \gamma _{COUNT(idL)}(LesAuteurs \bowtie_{LesAuteurs.idA = EcritPar.idA} EcritPar)$$
* **Code SQL :**
```sql
SELECT A.nom, COUNT(E.idL) as NombreDeLivres 
FROM LesAuteurs A 
JOIN EcritPar E ON A.idA = E.idA 
GROUP BY A.nom;
```

---

## 4. Requêtes bonus


### Requête 4 : Sous-requête d'exclusion (Livres disponibles)
* **En français :** Quels sont les identifiants et les titres des livres qui sont actuellement disponibles sur l'étagère (c'est-à-dire qui ne sont pas en cours d'emprunt) ?
* **Algèbre relationnelle :** $$\pi_{idL, titre}(LesLivres) - \pi_{idL, titre}(LesLivres \bowtie \sigma_{dateRetour \text{ IS NULL}}(LesEmprunts))$$
* **Code SQL :**
```sql
SELECT idL, titre 
FROM LesLivres 
WHERE idL NOT IN (
    SELECT idL 
    FROM LesEmprunts 
    WHERE dateRetour IS NULL
);
```

### Requête 5 : Jointures Multiples et Sélection (Emprunts en cours)
* **En français :** Quels sont les prénoms et noms des amis qui empruntent un livre en ce moment, ainsi que le titre du livre et la date de l'emprunt ?
* **Algèbre relationnelle :** $$\pi_{prenom, nom, titre, dateEmprunt}(\sigma_{dateRetour \text{ IS NULL}}(LesEmprunts \bowtie LesAmis \bowtie LesLivres))$$
* **Code SQL :**
```sql
SELECT LesAmis.prenom, LesAmis.nom, LesLivres.titre, LesEmprunts.dateEmprunt
FROM LesEmprunts
JOIN LesAmis ON LesEmprunts.idAm = LesAmis.idAm
JOIN LesLivres ON LesEmprunts.idL = LesLivres.idL
WHERE LesEmprunts.dateRetour IS NULL;
```

---

## 5. Implémentation Technique
La base de données SQLite a été générée via un script SQL, permettant de structurer les tables et d'y insérer un jeu de données réaliste. L'interrogation de cette base s'effectue via un programme Python (`DB.py`) utilisant la bibliothèque `sqlite3` pour se connecter au fichier `.db`, exécuter les requêtes en SQL, et afficher les résultats de manière lisible dans la console


# Annexe : 


### LesAuteurs
| idA | nom | prenom | nationalite | anNais |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Harari | Yaval | israélien | 1976 |
| 2 | Levit | Stephen | américain | 1967 |
| 3 | Kahneman | Daniel | américain | 1934 |
| 4 | Gladwell | Malcolm | anglais | 1963 |
| 8 | Rowling | Joan | anglaise | 1976 |
| 9 | MacHale | Donald | américain | 1955 |
| 10 | Giran | Paul | français | 1955 |

### LesLivres
| idL | titre | genre | anPub |
| :--- | :--- | :--- | :--- |
| 100 | Pendragon: The Merchant of Death | Fantasy | 2002 |
| 104 | Sapiens | Histoire | 2011 |
| 106 | Freakonomics | Économie | 2005 |
| 108 | Thinking, Fast and Slow | Psychologie | 2011 |
| 111 | Harry Potter à l'école des sorciers | Fantasy | 1997 |
| 114 | Think Again | Psychologie | 2021 |
| 116 | Psychologie du peuple annamite | Sociologie | 1904 |

### LesAmis
| idAm | nom | prenom | nationalite | email | anNais |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 200 | Chu | Quang | vietnamien | quang.chu2410@gmail.com | 2003 |
| 201 | Klymenchuk | Danylo | ukrainien | Dany.klymen@gmail.com | 2004 |
| 202 | Paller | Boldizsar | hongrie | boldi.thedump@gmail.com | 2003 |
| 204 | Melgren | William | Francais | willymel2201@gmail.com | 2005 |
| 208 | Do | Hai | vietnamien | boldi.thedump@gmail.com | 2003 |

### EcritPar
| idA | idL |
| :--- | :--- |
| 1 | 104 |
| 2 | 106 |
| 3 | 108 |
| 8 | 111 |
| 9 | 100 |
| 10 | 116 |

### LesEmprunts
| idL | idAm | dateEmprunt | dateRetour |
| :--- | :--- | :--- | :--- |
| 116 | 200 | 2025-10-01 | 2025-10-15 |
| 109 | 201 | 2025-11-05 | 2025-11-20 |
| 107 | 202 | 2025-12-01 | NULL |
| 111 | 204 | 2026-02-15 | NULL |
| 106 | 208 | 2026-03-10 | NULL |
| 114 | 208 | 2025-09-15 | 2025-10-10 |