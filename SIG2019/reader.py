#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import sys, time
from multiprocessing import Pool
import fonctions

def read(file: str, theme: str):
    """Fonction pour lire le fichier texte
    
    Parameters
    ----------
    file : str  
        Nom du fichier a lire
    theme : str
        Nom du theme analyse
    """

    frequences = dict()     # dictionnaire [mots] = frequences
    try:
        f = open(file, "r")     # open the file in reading mode
        if f.mode == 'r':
            content = f.readlines()
            # while there is still something to read
            for line in content:
                print(line)
                # split the line to obtain single words
                # and remove the uncesssesary words
                line = line.split(" ")      
                line = fonctions.remove_determinant(line)
                print(line)
                for word in line:
                    print(word)
                    frequences = fonctions.count_word(fonctions.radical(word), frequences)
                
                print("This is the new line ^^")
                
            fonctions.insert_db(frequences, theme)
        
        f.close()
    except IOError:
        print("No file with that name was found\n")
    finally:
        return 1
        

def main(argv):
    
    if argv[0] == "-h" or argv[0] == "help":
        print("usage reader.py <fileName> <themeName>\n")
        return 0

    read(argv[0], argv[1])

"""     with Pool(processes=1) as pool:
        res = pool.apply_async(read, (argv[0], argv[1]))
        waiting, n = True, 0
        print("Starting reading file\n")
        while waiting:
            try:
                waiting = not res.successful()
                data = res.get()
            except AssertionError:
                n = fonctions.loading_animation(n)
        sys.stdout.write("\r Finished reading file\n") """

if __name__ == "__main__":
    main(sys.argv[1:])