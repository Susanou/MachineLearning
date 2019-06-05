CREATE VIEW `moyennes` AS
    SELECT 
        total.Theme AS Theme, n / nDistinctWord AS moyenne
    FROM
        total
            INNER JOIN
        totalDistinct ON total.Theme = totalDistinct.Theme
    GROUP BY Theme