import nltk
from nltk import word_tokenize, pos_tag, sent_tokenize

def pos_sentence(sentence):
	word_tokens=word_tokenize(sentence)
	pos = pos_tag(word_tokens)
	print (pos)
	return pos;
'''
July/NNP and/CC August/NNP, all/DT your/PRP$ managers/NNS
 and/CC supervisors/NNS,company/NN courts/NNS and/CC adjudicators/NNS
'''
sentence=pos_sentence("July and Augest all your managers and supervisors company courts and adjudicators")
grammer =  "coordination:{<NNP><CC><NNP>+| <DT>?<PRP\$><NNS><CC><NNS>| <NN><NNS>+<CC><NNS> }" 
cp = nltk.RegexpParser(grammer)
result= cp.parse(sentence)
print (result)