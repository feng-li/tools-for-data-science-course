Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
nltk.download()
SyntaxError: multiple statements found while compiling a single statement
>>> import nltk
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True

>>> import csv
>>> nltk.download()
showing info https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/index.xml
True
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>> para = "I'm He Jieruo
SyntaxError: EOL while scanning string literal
>>> para = "I'm He Jieruo \nI love R"
>>> from nltk.tokenize import sent_tokenize
>>> sent_tokenize(para)
["I'm He Jieruo \nI love R"]
>>> para = "I'm He Jieruo . I love R"
>>> sent_tokenize(para)
["I'm He Jieruo .", 'I love R']
>>> from nltk.tokenize import word_tokenize
>>> word_tokenize(para)
['I', "'m", 'He', 'Jieruo', '.', 'I', 'love', 'R']
>>> 
