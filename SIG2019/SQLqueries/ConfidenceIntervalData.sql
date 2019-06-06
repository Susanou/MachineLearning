CREATE VIEW total AS
SELECT themes.nom as Theme, SUM(frequence) as n
FROM themes Inner JOIN frequences
ON frequences.theme = themes.id
group by Theme