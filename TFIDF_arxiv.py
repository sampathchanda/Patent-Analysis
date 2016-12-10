import os
import pandas as pd
import nltk
import sys
from sklearn.feature_extraction import text
import random
from sklearn.svm import SVC
import numpy as np
from operator import itemgetter

def importData(files):
    arxivData = pd.DataFrame(columns=['ID', 'Category', 'Title', 'Abstract'])
    for file in files:
        df = pd.read_csv(file, sep='\t', header=None, names=['ID', 'Category', 'Title', 'Abstract'])
        arxivData = arxivData.append(df, ignore_index=True)
    arxivData = arxivData[pd.notnull(arxivData['Abstract'])]
    for ind, cat in enumerate(arxivData['Category']):
        arxivData['Category'][ind] = cat.split()[0]
    categoryDict = {}
    categories = list(set(arxivData['Category']))
    for ind, cat in enumerate(categories):
        categoryDict[cat] = ind
    labels = [categoryDict[cat] for cat in arxivData['Category']]
    arxivData['Labels'] = labels

    print "Data Read"
    return arxivData

def tfGen(arxivData):
    tf = text.TfidfVectorizer(use_idf=False, analyzer='word', ngram_range=(1, 5), stop_words='english')
    abstractTf = tf.fit_transform(arxivData['Abstract'])

    print "TF marix generated"
    return (tf, abstractTf)

def tfidfGen(arxivData):
    tfidf = text.TfidfVectorizer(analyzer='word', ngram_range=(1, 5), stop_words='english')
    abstractTfidf = tfidf.fit_transform(arxivData['Abstract'])

    print "TFIDF matrix generated"
    return (tfidf, abstractTfidf)

def docAnalysis(tfidf, abstractTfidf):
    abstractFeatures = tfidf.get_feature_names()
    docs = random.sample(xrange(abstractTfidf.shape[0]), 100)
    print "Writing TFIDF scores to file"
    with open('AbstractAnalysis', 'w') as fd:
        for doc in docs:
            feature_index = abstractTfidf[doc,:].nonzero()[1]
            tfidf_scores = zip(feature_index, [abstractTfidf[doc, x] for x in feature_index])
            tfidf_scores = sorted(tfidf_scores, key=itemgetter(1))

            for word, score in [(abstractFeatures[i], score) for (i, score) in tfidf_scores[:10]]:
                fd.write(' ({}, {}) '.format(word, score))
            fd.write('\n')

def categoryPrediction(arxivData, abstractTfidf):
    randPerm = np.random.permutation(arxivData.shape[0])
    lenTrain = len(randPerm)*4/5
    trainInd = randPerm[:lenTrain]
    testInd = randPerm[lenTrain:]

    print "Training SVM"
    classifier = SVC(kernel='rbf')
    classifier.fit(abstractTfidf[trainInd][:], arxivData['Labels'].iloc[trainInd])
    pred = classifier.predict(abstractTfidf[testInd])
    accuracy = float(np.sum(pred == arxivData['Labels'].iloc[testInd]))/len(testInd)
    print "Test accuracy: {}".format(accuracy)


if __name__ == "__main__":
    arxivData = importData(sys.argv[1:])
    tfidf, abstractTfidf = tfidfGen(arxivData)
    docAnalysis(tfidf, abstractTfidf)
    categoryPrediction(arxivData, abstractTfidf)
    sys.exit()