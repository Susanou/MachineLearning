#!/usr/bin/env python3

"""Build a language detector model

The goal of this exercise is to train a linear classifier on text features
that represent sequences of up to 3 consecutive characters so as to be
recognize natural languages by using the frequencies of short character
sequences as 'fingerprints'.

"""
# Author: Olivier Grisel <olivier.grisel@ensta.org>
# License: Simplified BSD

import sys
import matplotlib.pyplot as plt
import argparse
import time
import pandas as pd
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB as naive
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import ComplementNB # as naive
from sklearn.svm import SVC as svc
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics
from urlReader import get_page

def predictSGD(): 

    start = time.time()

    clf = Pipeline([
        ('vect', vectorizer),
        ('clf', SGDClassifier(loss='log', penalty='l2',
                        alpha=1e-3, random_state=42,
                        max_iter=5, tol=None))
    ], verbose=True)

    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2), (1,3), (1,4), (1,5)],
        
        'clf__alpha': (1e-2, 1e-3, 5e-3, 7e-3, 4e-3, 3e-3, 2e-3, 8e-3, 9e-3),
    }

    gs_clf = GridSearchCV(clf, parameters, cv=5, iid=False, n_jobs=-1)
    gs_clf.fit(docs_train, y_train)

    print(gs_clf.best_params_)

    y_predicted = gs_clf.predict(docs_test)

    print("END...... total=%0.2f s" %(start-time.time()))

    # Print the classification report
    print(metrics.classification_report(y_test, y_predicted,
                                        target_names=dataset.target_names))

    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)


    plt.matshow(cm, cmap=plt.cm.jet)
    plt.show()

    # Predict the result on some wikipedia article:

    predicted = gs_clf.predict(articles)
    prob = gs_clf.predict_proba(articles)
    probs = np.argsort(prob, axis=1)[:,-3:]

    for pred in predicted:
        print("%s is the type of the text" % dataset.target_names[pred])

    frame1 = pd.DataFrame(probs, index=art_names)
    frame2 = pd.DataFrame(prob, index=art_names, columns=dataset.target_names)
    print(frame1)
    print(frame2)


#If using SVC, not able to get the the different proba of each case
def predictedSVC():
    start = time.time()

    clf = Pipeline([
        ('vect', vectorizer),
        ('clf', svc(tol=1e-3, verbose=0, random_state=42,
            C=1.0, max_iter=-1, gamma='scale', probability=True))
    ], verbose = True)

    parameters={
        'vect__ngram_range': [(1, 1), (1, 2), (1,3), (1,4), (1,5)],
        'clf__tol':(1e-3, 1e-2, 5e-3, 2e-3, 3e-3,4e-3),
        'clf__gamma':('auto', 'scale'),
        'clf__C':(1.0,.1,.2,.3,.4, 0.5, 0.6, 0.7, 0.8, 0.9)
    }

    gs_clf = GridSearchCV(clf, parameters, cv=5, iid=False, n_jobs=-1)
    gs_clf.fit(docs_train, y_train)

    y_predicted = gs_clf.predict(docs_test)

    print(gs_clf.best_params_)

    print("End.......... total=%.2f s" % (start - time.time()))

    # Print the classification report
    print(metrics.classification_report(y_test, y_predicted,
                                        target_names=dataset.target_names))

    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)


    plt.matshow(cm, cmap=plt.cm.jet)
    plt.show()

    # Predict the result on some wikipedia article:

    predicted = gs_clf.predict(articles)
    prob = gs_clf.predict_proba(articles)

    probs = best_n = np.argsort(prob, axis=1)[:,-3:]

    for pred in predicted:
        print("%s is the type of the text" % dataset.target_names[pred])

    frame1 = pd.DataFrame(probs, index=art_names)
    frame2 = pd.DataFrame(prob, index=art_names, columns=dataset.target_names)
    print(frame1)
    print(frame2)

def predictNaiveBayes():

    start = time.time()

    #MultinomialNB Pipeline
    clf = Pipeline([
        ('vect', vectorizer),
        ('clf', naive(alpha=1.0, fit_prior=True))
    ], verbose=True)

    parameters={
        'vect__ngram_range': [(1, 1), (1, 2), (1,3), (1,4), (1,5)],
        'clf__fit_prior': (True, False),
        'clf__alpha': (1.0, 0.1, 0.5, 2.0, .25, 0.75, 0.002),
    }

    gs_clf = GridSearchCV(clf, parameters, cv=5, iid=False, n_jobs=-1)
    gs_clf.fit(docs_train, y_train)

    print(gs_clf.best_params_)

    y_predicted = gs_clf.predict(docs_test)

    print("End.......... total=%.2f s" % (start - time.time()))

    # Print the classification report
    print(metrics.classification_report(y_test, y_predicted,
                                        target_names=dataset.target_names))

    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)



    plt.matshow(cm, cmap=plt.cm.jet)
    plt.show()

    # Predict the result on some wikipedia article:

    predicted = gs_clf.predict(articles)
    prob = gs_clf.predict_proba(articles)

    probs = best_n = np.argsort(prob, axis=1)[:,-3:]

    for pred in predicted:
        print("%s is the type of the text" % dataset.target_names[pred])

    frame1 = pd.DataFrame(probs, index=art_names)
    frame2 = pd.DataFrame(prob, index=art_names, columns=dataset.target_names)
    print(frame1)
    print(frame2)

if __name__ == "__main__":
    global languages_data_folder
    global dataset
    global docs_train, docs_test, y_train, y_test
    global vectorizer
    global articles
    global art_names

    parser = argparse.ArgumentParser(description="Script for fitting according to 3 different algorithms:\n SVC, Naive Bayes OR SGD")

    parser.add_argument("-n", "--naive", action="store_true", help='Use the Naive Bayes algorithm')
    parser.add_argument("-g", '--sgd', action='store_true', help="Use the SVG algorithm")
    parser.add_argument("-c", '--svc', action="store_true", help="Use the SVC algorithm")
    parser.add_argument("dataPath", default="dataFitting",nargs='?', type=str, help="Path to the folder where all the text data is stored")

    args = parser.parse_args()

    

    languages_data_folder = args.dataPath
    dataset = load_files(languages_data_folder)
    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.99, random_state=42, shuffle=True)
    vectorizer = TfidfVectorizer(ngram_range=(1,3), analyzer='word', use_idf=True)

    articles = [
        get_page('https://fr.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin'),
        get_page('https://fr.wikipedia.org/wiki/Victor_Hugo'),
        get_page('http://www.victor-hugo.info/'),
        get_page('https://www.babelio.com/auteur/mile-Zola/2168'),
        get_page('https://fr.wikipedia.org/wiki/Arthur_Rimbaud'),
        get_page('https://fr.wikipedia.org/wiki/Charles_Baudelaire'),
        get_page('https://fr.wikipedia.org/wiki/%C3%89mile_Zola')
    ]
    
    art_names=[
        'Chopin',
        'Hugo',
        'hugo',
        'zola',
        'Rimbaud',
        'baudelaire',
        'zola'
    ]

    if args.naive:
        print("Using naive bayes to fit")
        predictNaiveBayes()
    elif args.sgd:
        print("using sgd to fit")
        predictSGD()
    elif args.svc:
        print("Using SVC to fit")
        predictedSVC()
    else:
        parser.print_help()

    