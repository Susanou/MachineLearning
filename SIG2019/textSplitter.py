#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 06/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

from multiprocessing import Pool
from os.path import isfile, join

import sys, time, os

def writer(path: str, file: str):
    """Fonction pour couper les fichiers textes en fichiers de 500 mots chacun
    
    Parameters
    ----------
    path : str
        Chemin pour acceder au fichier
    file : str
        nom du fichier
    """
    try:
        f = open(file, "r")     # open the file in reading mode
        if f.mode == 'r':
            i = 1
            word = 0
            lines = f.readlines()

            while word < 1000 and i < 500:
                for line in lines:
                    line = line.split(" ")                        

                    for mot in line:
                        if word == 0:
                            new = file.split(".")
                            print(path+new[0]+"-%d.txt"%i)
                            w = open(path+new[0]+"-%d.txt"%i, 'w')
                        w.write(mot+" ")
                        word+=1

                        if word == 1000:
                            w.close()
                            word = 0
                            i += 1

                        if i == 500: # This is just to prevent too many files from being generated
                            break

                    if word == 1000:
                        w.close()
                        word = 0
                        i += 1
                    
                    if i == 500:
                        break
            
            w.close()
        
        f.close()
    except IOError:
        print("No file with that name was found\n")
    finally:
        return 1

def main(argv):
    if argv == None:
        print("usage textSplitter.py <pathName> <newPathName>\n")
        return 0

    if argv[0] == "-h" or argv[0] == "help":
        print("usage textSplitter.py <pathName> <newPathame>\n")
        return 0


    for x in os.listdir(argv[0]):
            if isfile(join(argv[0], x)):
                writer(argv[1], join(argv[0], x))  

if __name__ == "__main__":
    main(sys.argv[1:])