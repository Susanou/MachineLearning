CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `fukurou`@`localhost` 
    SQL SECURITY DEFINER
VIEW `sigma(n)k` AS
    SELECT 
        `pourcentage`.`mot` AS `Mot`,
        `pourcentage`.`cluster` AS `cluster`,
        STD(`pourcentage`.`pourcentage`) AS `STDDEV(pourcentage.pourcentage)`
    FROM
        `pourcentage`
    GROUP BY `pourcentage`.`mot` , `pourcentage`.`cluster`