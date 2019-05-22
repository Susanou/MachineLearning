#!/usr/bin/env python3

import sys
from . import utils

def main(argv):

    frequences = dict()


    print(argv[0])

def read(file: str, freq: dict):
    """
    Fonction pour lire les differents fichiers inputs
        :param file:str: nom du fichier a lire
    """

    # open file
    f = open(file, "r")
    if f.mode == 'r':
        line = f.readline()
        # while there is still something to read
        while line:
            content = line.split(" ")

            content = utils.remove_determinant(content)

            for word in content:
                utils.count_word(word, freq)


            

if __name__ == "__main__":
    main(sys.argv[1:])