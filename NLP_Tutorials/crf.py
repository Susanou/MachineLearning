#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Training tutorial on Conditional Random Fields
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import nltk
from sklearn.model_selection import train_test_split
from sklearn_crfsuite import CRF, metrics, scorers

tagged_sentence = nltk.corpus.treebank.tagged_sents(tagset='universal')
print(tagged_sentence)
print("Number of Tagged Sentences ",len(tagged_sentence))

tagged_words=[tup for sent in tagged_sentence for tup in sent]
#print(tagged_words)
print("Total Number of Tagged words", len(tagged_words))

vocab=set([word for word,tag in tagged_words])
print("Vocabulary of the Corpus",len(vocab))

tags=set([tag for word,tag in tagged_words])
print("Number of Tags in the Corpus ",len(tags))

train_set, test_set = train_test_split(tagged_sentence, test_size=0.2, random_state=1234)
print("Number of Sentences in Training Data ",len(train_set))
print("Number of Sentences in Testing Data ",len(test_set))


def features(sentence, index):
    """Fonction pour donner un tag a chaque mot d'une phrase
    
    Parameters
    ----------
    sentence : list
        liste de mots
    index : int
        position du mot dans la phrase
    """
    
    return{
        'is_first_Capital':int(sentence[index][0].isupper()),
        'is_first_word':int(index==0),
        'is_last_word':int(index==len(sentence)-1),
        'is_complete_capital':int(sentence[index].upper()==sentence[index]),
        'prev_word':'' if index==0 else sentence[index],
        'next_word':'' if index==len(sentence)-1 else sentence[index+1],
        'is_numeric':int(sentence[index].isdigit()),
        'is_alphanumeric':int(sentence[index].isalnum()),
        'prefix_1':sentence[index][0],
        'prefix_2':sentence[index][:2],
        'prefix_3':sentence[index][:3],
        'prefix_4':sentence[index][:4],
        'suffix_1':sentence[index][-1],
        'suffix_2':sentence[index][-2:],
        'suffix_3':sentence[index][-3:],
        'suffix_4':sentence[index][-4:],
        'has_hyphen':1 if '-' in sentence[index] else 0
    }

def untag(sentence):
    return[word for word, tag in sentence]

def prepData(tagged_sentences):
    X,y=[],[]
    
    for sentences in tagged_sentences:
        X.append([features(untag(sentences), index) for index in range(len(sentences))])
        y.append([tag for word, tag in sentences])
    return X, y

X_train,y_train=prepData(train_set)
X_test, y_test = prepData(test_set)

crf = CRF(
    algorithm='lbfgs',
    c1=0.01,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)

crf.fit(X_train, y_train)

y_pred=crf.predict(X_test)
print("F1 score on Test Data ")
print(metrics.flat_f1_score(y_test, y_pred, average='weighted', labels=crf.classes_))
print("F score on Training data ")
y_pred_train = crf.predict(X_train)
metrics.flat_f1_score(y_train, y_pred_train, average='weighted', labels=crf.classes_)

print(metrics.flat_classification_report(
    y_test, y_pred, labels=crf.classes_, digits=3
))