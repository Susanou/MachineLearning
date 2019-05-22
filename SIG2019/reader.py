#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import sys, time, threading
import fonctions

def main(argv):

    frequences = dict()


    print(argv[0])

def read(file: str, freq: dict):
    """
    Fonction pour lire les differents fichiers inputs et ajouter la frequence des mots
        :param file:str: nom du fichier a lire
    """

    # open file
    f = open(file, "r")
    if f.mode == 'r':
        line = f.readline()
        # while there is still something to read
        while line:
            content = line.split(" ")

            content = fonctions.remove_determinant(content)

            for word in content:
                fonctions.count_word(fonctions.radical(word), freq)
            
    


            

if __name__ == "__main__":
    main(sys.argv[1:])