CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `fukurou`@`localhost` 
    SQL SECURITY DEFINER
VIEW `distance1` AS
    SELECT 
        (`pourcentage`.`pourcentage` - AVG(`moyennes`.`moyenne`)) AS `distance`,
        `sigma(n)`.`sigma` AS `sigma`
    FROM
        ((`pourcentage`
        JOIN `sigma(n)` ON ((`pourcentage`.`mot` = `sigma(n)`.`Mot`)))
        JOIN `moyennes` ON ((`moyennes`.`Theme` = `pourcentage`.`theme`)))