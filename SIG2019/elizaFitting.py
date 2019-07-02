#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import sys
import matplotlib.pyplot as plt
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB as naive
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics
from urlReader import get_page

dataset = load_files('dataFitting')

docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.25, random_state=42, shuffle=True)

def fitting1():

    vectorizer = TfidfVectorizer(ngram_range=(1,3), analyzer='word', use_idf=True)

    clf = Pipeline([
        ('vect', vectorizer),
        ('clf', SGDClassifier(loss='log', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None))
    ])

    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2), (1,3), (1,4), (1,5)],
        
        'clf__alpha': (1e-2, 1e-3, 5e-3, 7e-3, 4e-3, 3e-3, 2e-3, 8e-3, 9e-3),
    }
    gs_clf = GridSearchCV(clf, parameters, cv=5, iid=False, n_jobs=-1)

    gs_clf.fit(docs_train, y_train)

    return gs_clf, dataset.target_names

def fitting2():

    dataset = load_files('dataFitting')

    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.25, random_state=42, shuffle=True)

def max(prob):
    max=prob[0]
    maxi=0
    for i, p in enumerate(prob):
        if max < p:
            max = p
            maxi = i

    return maxi

def vote(prob1, prob2, prob3):
    """Fonction nous permettant de voter sur le resulat en cas d'absence de choix
    
    Parameters
    ----------
    prob1 : array-like
        liste de probabilite pour chaque classe selon le premier algorithme
    prob2 : array-like
        liste de probabilite pour chaque classe selon le deuxieme algorithme
    prob3 : array-like
        liste de probabilite pour chaque classe selon le troisieme algorithme
    
    Returns
    -------
    int or list
        Renvoi soit l'indexe du resultat ou une liste des resultats les plus probables
    """

    top1 = np.argsort(prob1, axis=1)[:,-3:]
    top2 = np.argsort(prob2, axis=1)[:,-3:]
    top3 = np.argsort(prob3, axis=1)[:,-3:]

    if top1[2] == top2[2] and top1[2] == top3[2]:
        return top1[2]
    elif top1[2] == top2[2]:
        return top1[2]
    elif top1[2] == top3[2]:
        return top1[2]
    elif top2[2] == top3[2]:
        return top2[2]
    else:
        common = list()
        for i in top1:
            for j in top2:
                for k in top3:
                    if i==k:
                        common.append(i)
                    elif i==j:
                        common.append(i)
                    elif j==k:
                        common.append(j)
        
        return common