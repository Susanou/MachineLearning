CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `fukurou`@`localhost` 
    SQL SECURITY DEFINER
VIEW `variance` AS
    SELECT 
        `frequences`.`mot` AS `Mot`,
        VARIANCE(`frequences`.`frequence`) AS `Variance`
    FROM
        `frequences`
    GROUP BY `frequences`.`mot`