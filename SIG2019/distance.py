#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 06/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import fonctions_bot as fonctions

def distance1(theme: str, cluster: str, n: int):
    """Fonction pour notre deuxieme algorithme de distance 
        entre un theme et un cluster
    
    Parameters
    ----------
    theme : str
        Id du theme
    cluster : str
        Id du cluster
    n : int
        nombre de point a selectionne
    
    Returns
    -------
    float
        Renvoi la distance entre l'article et le theme
    """
    
    db = fonctions.connectDB()
    cursor = db.cursor()

    query = (
        """
        SELECT 
            pourcentage, sigma
        FROM
            pourcentage
                JOIN
                `sigma(n)` ON pourcentage.mot = `sigma(n)`.mot
        WHERE pourcentage.theme = %d
        ORDER BY sigma DESC
        LIMIT %d
        """
    )

    cursor.execute(query % (theme, n))
    articles = cursor.fetchall()

    query = (
        """
        SELECT 
            AVG(moyenne)
        FROM
            moyennes
                JOIN
            themes ON moyennes.Theme = themes.nom
        WHERE
            themes.cluster = %d
        """
    )

    cursor.execute(query % (cluster))
    moy = float(cursor.fetchone()[0])
    
    total = float()

    for article in articles:
        total += abs(float(article[0]) - moy) 

    return total

def distance2(theme: str, cluster: str, n: int):
    db = fonctions.connectDB()
    cursor = db.cursor()

    query = (
        """
        SELECT 
            pourcentage, sigma
        FROM
            pourcentage
                JOIN
                `sigma(n)` ON pourcentage.mot = `sigma(n)`.mot
        WHERE pourcentage.theme = %d
        ORDER BY sigma DESC
        LIMIT %d
        """
    )

    cursor.execute(query % (theme, n))
    articles = cursor.fetchall()

    query = (
        """
        SELECT 
            AVG(moyenne)
        FROM
            moyennes
                JOIN
            themes ON moyennes.Theme = themes.nom
        WHERE
            themes.cluster = %d
        """
    )

    cursor.execute(query % (cluster))
    moy = float(cursor.fetchone()[0])
    
    total = float()

    for article in articles:
        total += (float(article[0]) - moy)**2

    return total


def distance3(theme: str, cluster: str, n: int):
    """Fonction pour notre troisieme algorithme de distance 
        entre un theme et un cluster
    
    Parameters
    ----------
    theme : str
        Id du theme
    cluster : str
        Id du cluster
    n : int
        nombre de point a selectionne
    
    Returns
    -------
    float
        Renvoi la distance entre l'article et le theme
    """
    
    db = fonctions.connectDB()
    cursor = db.cursor()

    query = (
        """
        SELECT 
            pourcentage, sigmaKN, sigma
        FROM
            pourcentage
                JOIN
                `sigma(n)k` ON pourcentage.mot = `sigma(n)k`.mot
                JOIN `sigma(n)` ON pourcentage.mot = `sigma(n)`.mot
        WHERE pourcentage.theme = %d
        ORDER BY sigma DESC
        LIMIT %d
        """
    )

    cursor.execute(query % (theme, n))
    articles = cursor.fetchall()

    query = (
        """
        SELECT 
            AVG(moyenne)
        FROM
            moyennes
                JOIN
            themes ON moyennes.Theme = themes.nom
        WHERE
            themes.cluster = %d
        """
    )

    cursor.execute(query % (cluster))
    moy = float(cursor.fetchone()[0])
    
    total = float()

    for article in articles:
        if float(article[1]) != 0:
            total += 1/float(article[1])*abs(float(article[0]) - moy) 

    return total