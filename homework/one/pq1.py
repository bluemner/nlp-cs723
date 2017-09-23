'''
Author: brandon Bluemner
'''
# %%
import nltk
from collections import defaultdict, Counter
# corpus = GetCorpus(nltk.corpus.brown, 'news')
# cfd = GetAmbiguousWords(corpus, 4)
# TestGetAmbiguousWords(cfd, 4)
# Showexample_helps('book', cfd, corpus)


def GetCorpus(corpus_name, category_name):
    '''
            returns: the tagged words
            for that corpus and category,
            so that you can call the remaining
            functions without repeating this work.
    '''

    return corpus_name.tagged_words(categories=category_name);


def GetAmbiguousWords(corpus, N=0):
    '''
    Write a function GetAmbigousWords(corpus,N) that nds words
    in the corpus with more than N observed tags. This function
    should return a ConditionalFreqDist object where the conditions
    are the words and the frequency distribution indicates the tag
    frequencies for each word.
    '''
    word_dict = defaultdict(set)
    for (word, tag) in corpus:
        word_dict[word].add(tag)
    filtered_words = [(word, tag)
                       for (word, tag) in corpus if len(word_dict[word]) > N]

    return nltk.ConditionalFreqDist(filtered_words);


def TestGetAmbiguousWords(cfd, N=0):
     state = True
     for word in cfd.conditions():
         state &= (len(cfd[word]) > N)
     return 'All words occur with more than {} tags.'.format(N) if state else 'A words occur with less than or equal to {} tags.'.format(N);


def ShowExample(word, cfd, corpus):
    '''
    Write a function ShowExample(word,corpus) that given a word,
    nds one example_help of usage of the word with each of the different
    tags in which it can occur. (The corpus can be the tagged Sentences
    or tagged words according to what is most convenient)
    '''
    for tag in cfd[word].keys():
        corpus_index = corpus.index((word, tag))
        sent = corpus[corpus_index - 10:corpus_index] + \
            [(word.upper(), tag)] + corpus[corpus_index + 1:corpus_index + 11]
        helper = ' '.join(word for (word, tag) in sent)
        print('ShowExample\n\t\'{}\' => {}: {}'.format(word, tag, helper))
    return ' ';

# %%
corpus=GetCorpus(nltk.corpus.brown, 'news')
# print(corpus)
cfd=GetAmbiguousWords(corpus)
test=TestGetAmbiguousWords(cfd, 1)
ShowExample('book', cfd, corpus)
ShowExample('news', cfd, corpus)
print(cfd)
print(test)
