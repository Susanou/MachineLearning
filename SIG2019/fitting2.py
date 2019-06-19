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

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics
from urlReader import get_page

# The training data folder must be passed as first argument
languages_data_folder = sys.argv[1]
dataset = load_files(languages_data_folder)

# Split the dataset in training and test set:
docs_train, docs_test, y_train, y_test = train_test_split(
    dataset.data, dataset.target, test_size=0.99, random_state=42, shuffle=True)


# TASK: Build a vectorizer that splits strings into sequence of 1 to 3
# characters instead of word tokens
vectorizer = TfidfVectorizer(ngram_range=(1,3), analyzer='word', use_idf=True)

# TASK: Build a vectorizer / classifier pipeline using the previous analyzer
# the pipeline instance should stored in a variable named clf
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

# TASK: Fit the pipeline on the training set
#clf.fit(docs_train, y_train)

# TASK: Predict the outcome on the testing set in a variable named y_predicted
y_predicted = gs_clf.predict(docs_test)

# Print the classification report
print(metrics.classification_report(y_test, y_predicted,
                                    target_names=dataset.target_names))

# Plot the confusion matrix
cm = metrics.confusion_matrix(y_test, y_predicted)
print(cm)


plt.matshow(cm, cmap=plt.cm.jet)
#plt.show()

# Predict the result on some wikipedia article:

articles = [
    get_page('https://fr.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Chopin'),
    get_page('https://fr.wikipedia.org/wiki/Victor_Hugo'),
    get_page('http://www.victor-hugo.info/'),
    get_page('https://www.babelio.com/auteur/mile-Zola/2168')
]

predicted = gs_clf.predict(articles)
probs = gs_clf.predict_proba(articles)

for pred in predicted:
    print("%s is the type of the text" % dataset.target_names[pred])

for i, x in enumerate(probs):
    for j, prob in enumerate(x):
        print("these are the probablities in %d for %s: %.2f"% (i, dataset.target_names[j], prob*100))
