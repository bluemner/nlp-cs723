#import nltk

# STEP 1 run this first to get information
# nltk.download()
import nltk
nltk.data.path.append("L:\\nltk_data")
from nltk.tokenize import sent_tokenize, word_tokenize

example_text  = "Some very stupid text. This is really dumb and am not sure that this going to be good?"

print (sent_tokenize(example_text))

for i in word_tokenize(example_text):
	print(i)
