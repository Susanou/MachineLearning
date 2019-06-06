CREATE VIEW `confiance` AS
    SELECT 
        top, bottom, word.mot AS Mot, themes.nom AS Theme
    FROM
        intervals,
        word,
        themes
    WHERE
        intervals.mot = word.id
            AND intervals.theme = themes.id;
