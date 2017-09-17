"""
	Plan text corpus reader 
"""
import nltk
nltk.data.path.append("L:\\nltk_data")

from nltk.corpus import PlaintextCorpusReader

text_folder = '../data/'
wordlist = PlaintextCorpusReader(text_folder,'.*')
print(wordlist.fileids())
file_name ='a.txt'
print(wordlist.words(file_name))
