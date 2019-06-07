CREATE VIEW `pourcentage` AS
    SELECT 
        frequences.mot, frequences.frequence / total.n*10000 AS pourcentage
    FROM
        frequences,
        total
    WHERE
        frequences.theme = (SELECT 
                id
            FROM
                themes
            WHERE
                themes.nom = total.Theme)