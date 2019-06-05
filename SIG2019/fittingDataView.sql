CREATE VIEW fittingData AS
    SELECT 
        frequences.mot AS mot,
        frequences.theme AS theme,
        frequences.frequence AS frequence,
        variance.Variance
    FROM
        frequences
            INNER JOIN
        variance ON frequences.mot = variance.Mot
            AND variance.Variance > 4
    ORDER BY frequence DESC