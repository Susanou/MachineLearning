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

class Eliza:
    """Class contenant les differentes fonctions du chatbot
    """
    def __init__(self, *args, **kwargs):
        self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
        self.values = list(map(lambda x:x[1],gPats))

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

        for i in range(0, len(words)):
            if words[i] in keys:
                words[i] = keys[words[i]]

        return ' '.join(words)

    def reponse(self, str:str):
        """Fonction permettant au bot de repondre a l'utilisateur
        
        Parameters
        ----------
        str : str
            input de l'utilisateur

        Returns
        -------
        str
            renvoi la reponse du bot
        """

        for i in range(0, len(self.keys)):
            match = self.keys[i].match(str)
            if match:
                rep = random.choice(self.values[i])

                pos = rep.find('%')
                while pos > -1:
                    num = int(rep[pos+1:pos+2])
                    rep = rep[:pos] + \
                        self.traduire(match.group(num), traductions) + \
                            rep[pos+2:0]
                    pos = rep.find('%')

                if rep[-2:] == '?.' : rep = rep[:-2] + '.'
                if rep[-2:] == '??' : rep = rep[:-2] + '?'

                return rep


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

    [r"Qu'est ce (*.)",
    [   "Pourquoi demandez-vous?",
        "Comment cela vous aiderai?",
        "Qu'en pensez-vous?"]],

    [r"Bonjour(.*)",
    [   "Bonjour. Ravi que vous ayez pu venir aujourd'hui.",
        "Bonjour, comment allez-vous?"]],

    [r"Je pense (*.)",
    [   "Doutez-vous %1?",
        "Pensez-vous vraiment %1?",
        "Mais vous n'etes pas sur %1?"]],

    [r"Oui",
    [   "Vous avez l'ai sur de vous.",
        "Pouvez vous developer un peu plus?"]],
    
    [r"J'ai (.*)",
    [   "Pourquoi me dites vous que vous avez %1?",
        "Avez vous vraiment %1?",]],
    
]


def interface():
    print('SIG 2019\n-----------------------')
    print('Parlez au programme en francais en utilisant')
    print('majuscules et minuscules comme dans la vie courante.')
    print('Tapez "exit" ou "quit" une fois fini')

    s = ''
    bot = Eliza()
    while s != 'quit' or s != 'exit':
        try:
            s = input('> ')
        except EOFError:
            s = 'quit'
        print(s)
        while s[-1] in '!.':
            s = s[:-1]
        print(bot.reponse(s))

if __name__ == "__main__":
    interface()