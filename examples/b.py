"""
 Frequency distribution
"""
import nltk
nltk.data.path.append("L:\\nltk_data")
from nltk import word_tokenize, FreqDist
words = "I went the mall today and the person at the store was lame."
fdist = FreqDist(word_tokenize(words))
print(fdist)
print(fdist['the'])
