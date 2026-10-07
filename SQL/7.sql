SELECT Livre.titre, Auteur.nom
FROM Livre
INNER JOIN Auteur ON Livre.id_auteur = Auteur.id_auteur;