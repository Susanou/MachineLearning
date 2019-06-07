#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Training on uing NLTK for our chatbot
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

#################
# Tokenize Text #
#################

from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import urllib.request
import nltk

response = urllib.request.urlopen('https://fr.wikipedia.org/wiki/Victor_Hugo')
html = response.read()
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip=True)

tokens = [t for t in text.split()]
freq = nltk.FreqDist(tokens)
for key,val in freq.items():
    pass
#    print(str(key) + ':' + str(val))


clean_tokens = tokens[:]
sr = stopwords.words('french')

#print(sr)

for token in tokens:
    if token in sr:
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    pass
#    print(str(key) + ':' + str(val))

freq.plot(20, cumulative=False)

1
2
3
4
5
	
from nltk.stem import SnowballStemmer
 
french_stemmer = SnowballStemmer('french')
 
print(french_stemmer.stem("totalement"))