"""
Bigrams and collocations .
"""

import nltk
nltk.data.path.append("L:\\nltk_data")

from nltk.collocations import *

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(nltk.corpus.brown.words())

# point wise mutual information
temp = finder.nbest(bigram_measures.pmi, 10)
print(temp)