# %%
import nltk
from nltk import word_tokenize, pos_tag, sent_tokenize

def pos_sentence(sentence):
	word_tokens=word_tokenize(sentence)
	pos = pos_tag(word_tokens)
	print (pos)
	return pos;

sentence=pos_sentence("many researchers two weeks both new positions")
#[("many", "JJ"), ("researchers", "NNS"), ("two", "CD"), ("weeks", "NNS"), ("both","DT"), ("new", "JJ"), ("positions", "NNS")]
grammer = "NP:{<CD>?<DT>?<JJ>*<NNS>+}"
cp = nltk.RegexpParser(grammer)
result= cp.parse(sentence)


print (result)

# the/DT receiving/VBG end/NN, assistant/NN managing/VBG editor/NN.
sentence=pos_sentence("the receiving end assistant managing editor")
grammer = "gerunds:{<NN>?<DT>?<VBG><NN>}"
cp = nltk.RegexpParser(grammer)
result= cp.parse(sentence)
print (result)

