#import nltk
import nltk
# STEP 1 run this first to get information
# nltk.download()

# If you put nltk in a diffrent folder then you might
#	tell python the data folder location.
nltk.data.path.append("L:\\nltk_data")
# Import other packages from python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example that I have no clue if it is going to work for what I am trying."

stop_words = set(stopwords.words("english"))

# print(stop_words)

words = word_tokenize(example_sentence)


# filtered_sentence = []

# for w in words:
# 	if w not in stop_words:
# 		filtered_sentence.append(w)


filtered_sentence = [w for w in words if not w in stop_words]
print(filtered_sentence)