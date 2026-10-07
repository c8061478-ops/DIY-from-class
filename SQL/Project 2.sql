SELECT Adherent.nom, Livre.titre
FROM Emprunt
INNER JOIN Livre ON Emprunt.isbn = Livre.isbn
INNER JOIN Adherent ON Emprunt.id_adherent = Adherent.id_adherent
WHERE Emprunt.date_retour IS NULL