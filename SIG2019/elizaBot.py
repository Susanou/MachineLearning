#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import random
import string
import re
import fonctions_bot as fonctions
import numpy as np

from elizaFitting import fitting1, fitting2,fitting3
from elizaFitting import vote

class Eliza:
    """Class contenant les differentes fonctions du chatbot
    """
    def __init__(self):
        self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
        self.values = list(map(lambda x:x[1],gPats))
        self.freq = dict()
        #self.clf1, self.names = fitting1()
        #self.clf2 = fitting2()
        #self.clf3 = fitting3()
        self.talk = list()
        self.log = list()

    def traduire(self, str:str, dict:dict):
        """Fonction permettant de 'traduire' certains mots
        comme 'je' --> 'tu' etc.
        
        Parameters
        ----------
        str : str
            mot a traduire
        dict : dict
            dictionnaire contenant les mots et leur traduction correspondante

        Returns
        -------
        str
            mot 'traduit'
        """

        words = str.lower().split()
        keys = dict.keys()

        for i in range(0,len(words)):
            if words[i] in keys:
                words[i] = dict[words[i]]

        return ' '.join(words)

    def reponse(self, str:str):
        """Fonction permettant au bot de repondre a l'utilisateur
        
        Parameters
        ----------
        str : str
            input de l'utilisateur utilise comme base pour repondre
        
        Returns
        -------
        str
            Renvoi la reponse de ELIZA
        """
        log = str

        r = random.random()
        p = 0.2 # probabilite de retour sur une question precedente
        q = 0.4 # probabilite pour selectionne de combien on fait le retour

        if r < p and len(self.log) > 3:
            back = 1
            s = q
            print(r/p>s)
            while r/p > s and back < 5 and back < len(self.log) - 1:
                s += q**back                
                back += 1

            str = self.log[-back]
            
            self.log.append(log)

            print()
            print(self.log)
            print("going back to #", back)
        else:
            self.log.append(log)

        for i in range(0, len(self.keys)):
            match = self.keys[i].match(str)
            if match:
                rep = random.choice(self.values[i])

                pos = rep.find('%')
                while pos > -1:
                    num = int(rep[pos+1:pos+2])
                    rep = rep[:pos] + \
                        self.traduire(match.group(num), traductions) + \
                        rep[pos+2:]
                    pos = rep.find('%')
                # fix munged punctuation at the end
                if rep[-2:] == '?.': rep = rep[:-2] + '.'
                if rep[-2:] == '??': rep = rep[:-2] + '?'
                return rep

    def search(self, s:str):
        """Fonction pour chercher le theme de la phrase
        
        Parameters
        ----------
        str : str
            phrase de l'utilisateur
        """
        if len(self.talk) > 0:
            self.talk[0] += " " + s
        else:
            self.talk.append(s)
        
        pred1 = self.clf1.predict_proba(self.talk)
        pred2 = self.clf2.predict_proba(self.talk)
        pred3 = self.clf3.predict_proba(self.talk)

        #pred3 = np.array([1e-5, 1e-5, 1e-5])

        result = vote(pred1, pred2, pred3)
        
        print("resultat du vote: ", result)

        for i in np.nditer(result, flags=["refs_ok"]):
            print(i)
            if len(str(i)) > 1:
                for j in i:
                    print(j)
                    print("resultat du vote: ", self.names[int(j)])
            else:
                print(i)
                print("resultat du vote: ", self.names[int(i)])

        return self.reponse(s)

        


# Dictionnaire avec des conjugaisons communes devant etre changees
traductions = {
    "suis": "êtes",
    "je":"vous",
    "mon":"votre",
    "mes":"vos",
    "moi":"vous",
    "j'ai":"vous avez"
}

# Dictionaire contenant les reponses principales de ELIZA
# La premiere partie est une regex
# La second est une liste de reponses possible avec 
# %1, %2.... comme pattern pour recuperer les groupes de textes
gPats = [
    [r"J'ai besoin de (.*)",
    [   "Pourquoi avez vous besoin de %1?",
        "Est-ce-que obtenir %1 vous aiderai vraiment?",
        "Etes-vous sur d'avoir besoin de 1%?"]],

    [r"Pourquoi (?:ne puis-je|je ne peux) ([^\?]*)\??",
    [   "Pourquoi ne pouvez vous pas %1?",
        "Si vous pouviez %1, que feriez vous?",
        "Je ne sais pas -- Pourquoi ne pouvez vous pas %1?",
        "Avez vous essayer?"]],
    
    [r"Je ne peux (?:pas) ([^\?]*)\??",
    [   "Comment savez vous que vous ne pouvez pas %1?",
        "Peut etre que vous pouriez %1 si vous essaieriez.",
        "Que faudrait-t-il pour que vous puissiez %1?"]],

    [r"Je suis (.*)",
    [   "Etes vous venu vers moi parce que vous etes %1?",
        "Depuis combien de temps etes vous %1?",]],
    
    [r"(?:Estes-vous|Est-ce-que vous etes) ([^\?]*)\??",
    [   "Prefereriez-vous que je ne sois pas %1?",
        "Peut-etre pensez vous que je suis %1?",
        "Je le suis peut-etre -- Qu'en pensez vous?",]],

    [r"Parce que (.*)",
    [   "Est-ce la vraie raison?",
        "A quelles autres raisons pouvez vous penser?",
        "Si %1, alors quoi d'autre est vrai?",]],

    [r"(.*) (?:pardon|excusez) (.*)",
    [   "Pourquoi vous excusez-vous?",
        "Qu'est ce qui fait que vous vous excusez?"]],

    [r"Qu'est ce (.*)",
    [   "Pourquoi demandez-vous?",
        "Comment cela vous aiderai?",
        "Qu'en pensez-vous?"]],

    [r"Bonjour(.*)",
    [   "Bonjour. Ravi que vous ayez pu venir aujourd'hui.",
        "Bonjour, comment allez-vous?"]],

    [r"Je pense (.*)",
    [   "Doutez-vous %1?",
        "Pensez-vous vraiment %1?",
        "Mais vous n'etes pas sur %1?"]],

    [r"Oui",
    [   "Vous avez l'ai sur de vous.",
        "Pouvez vous developer un peu plus?"]],
    
    [r"J'ai (.*)",
    [   "Pourquoi me dites vous que vous avez %1?",
        "Avez vous vraiment %1?",]],

    [r"(.*) (?:papa|pere) (.*)",
    [   "Parlez moi plus de votre pere?",
        "Comment vous sentez vous a propos de votre pere?",
        "Avez-vous des problemes pour montrer vos sentiments a vos parents?"]],

    # Insert new sentences here ^
    # Below are the cases where we have no other options

    
    [r"(.*)\?",
    [   "Pourquoi demandez vous ca?",
        "Pourquoi ne me le dites vous pas vous meme?",
        "La reponse ce trouve peut etre en vous?"]],

    [r"(?:quit|exit)",
    [   "Au revoir",
        "Ce sera 200$. Par espece ou par carte?",
        "Merci d'etre venu me parler."]],

    [r"(.*)",
    [   "Dites m'en plus.",
        "Je vois",
        "%1",
        "Pouvez vous developer un peu plus?",
        "Comment vous sentez vous suite a cela?"]]
    
]

def interface():
    print('SIG 2019\n-----------------------')
    print('Parlez au programme en francais en utilisant')
    print('majuscules et minuscules comme dans la vie courante.')
    print('Tapez "exit" ou "quit" une fois fini')

    print('='*80)
    print("Bonjour comment allez vous aujourd'hui?\n")

    s = ''

    therapist = Eliza()
    next = True
    while next:
        try:
            s = input('> ')
        except EOFError:
            s = 'quit'
            print(s)
        while s[-1] in '!.':
            s = s[:-1]
        print(therapist.reponse(s))

        if s == 'quit' or s == 'exit':
            next = False


if __name__ == "__main__":
    interface()