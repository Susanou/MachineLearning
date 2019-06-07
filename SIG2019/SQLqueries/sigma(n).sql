CREATE VIEW `sigma(n)` AS
    SELECT 
        pourcentage.mot AS Mot,
        STDDEV(pourcentage.pourcentage) AS sigma
    FROM
        pourcentage
    GROUP BY Mot