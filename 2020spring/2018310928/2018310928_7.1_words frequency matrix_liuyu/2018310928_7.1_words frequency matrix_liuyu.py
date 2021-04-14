from collections import Counter
from itertools import chain
import numpy as np
documents = ["Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment",
             "Older people and those with underlying medical problems like cardiovascular disease diabetes chronic respiratory disease and cancer are more likely to develop serious illness",
             "The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads",
             "Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face",
             "The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes",
             "At this time there are no specific vaccines or treatments for COVID-19",
             "However there are many ongoing clinical trials evaluating potential treatments",
             "WHO will continue to provide updated information as soon as clinical findings become available",]

def word_matrix(documents):
    '''Build a dictionary'''
    doc = [d.lower() for d in documents]
    doc = [d.split() for d in doc]
    words = list(set(chain(*doc)))
    dictionary = dict(zip(words, range(len(words))))
    
    '''generate a matrix to store the numbers'''
    matrix = np.zeros((len(words), len(doc)))
    
    '''calculate the frequency of each word'''
    for col, d in enumerate(doc):  
        count = Counter(d)
        for word in count:
            id = dictionary[word]
            matrix[id, col] = count[word]
    return matrix, dictionary
 
matrix, dictionary = word_matrix(documents)
print(matrix,'\n',dictionary)
