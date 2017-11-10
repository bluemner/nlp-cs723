import nltk

from nltk import word_tokenize, pos_tag, sent_tokenize

def pos_sentence(sentence):
	word_tokens=word_tokenize(sentence)
	pos = pos_tag(word_tokens)
	print (pos)
	return pos;
words ="All I know is that I stood spellbound in his high-ceilinged studio room, with its north-facing windows in front ofthe heavy mahogany bureau at which Michael said he no longer worked because the room was so cold, even inmidsummer; and that, while we talked of the difficulty of heating old houses, a strange feeling came upon me, as ifit were not he who had abandoned that place of work but I, as if the spectacles cases, letters and writing materialsthat had evidently lain untouched for months in the soft north light had once been my spectacle cases, my letters andmy writing materials."

pos_sentence(words)