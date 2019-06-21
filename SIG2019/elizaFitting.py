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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics
from urlReader import get_page

def fitting():
    
    dataset = load_files('dataFitting')

    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.5, random_state=42, shuffle=True)

    vectorizer = TfidfVectorizer(ngram_range=(1,3), analyzer='word', use_idf=True)

    clf = Pipeline([
        ('vect', vectorizer),
        ('clf', SGDClassifier(loss='log', penalty='l2',
                          alpha=1e-3, random_state=42,
                          max_iter=5, tol=None))
    ])

    parameters = {
    'vect__ngram_range': [(1, 1), (1, 2)],
    'clf__alpha': (1e-2, 1e-3),
    }

    gs_clf = GridSearchCV(clf, parameters, cv=5, iid=False, n_jobs=-1)

    gs_clf.fit(docs_train, y_train)

    return gs_clf, dataset.target_names