CREATE VIEW `totalDistinct` AS
SELECT themes.nom as Theme, COUNT(DISTINCT mot) as nDistinctWord
FROM themes Inner JOIN frequences
ON frequences.theme = themes.id
group by Theme