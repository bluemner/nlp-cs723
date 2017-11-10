from __future__ import division
import sys
from pprint import pprint
from collections import defaultdict
import nltk
#nltk file on my L drive
nltk.data.path.append("L:\\nltk_data\\")
from nltk.corpus import treebank
from nltk import ConditionalFreqDist, Nonterminal, FreqDist
from fixesNLTK3 import *
from BetterICP import *
from nltk import InsideChartParser
import sys,os
def print_tree(itr):
    pass
def read_from_file(file_name):
  input_file = open(file_name,"r")
  text =[]
  for line in input_file:
    text.append(line)
  input_file.close()
  return text
def write_line_to_file(file_name, line):
  out_file = open(file_name,"a")
  out_file.write(line)
  out_file.close()

def main():
  #disgusting hack to override output to file
  f = open("hw2_output.txt", "w")
  f.write("")
  f.close()
  sys.stdout = open("hw2_output.txt", "a")
  ## Main body of code ##
  # Extracting tagged sentences using NLTK libraries
  psents = treebank.parsed_sents()
  #print(psents)
  # Comment out the following 3 lines if you get tired ofc seeing them
  write_line_to_file ("hw2_output.txt" ,"\n 1st parsed sentence: {} \n".format(psents[0]))
  write_line_to_file ("hw2_output.txt" ,"\n Productions in the 1st parsed sentence: \n")
  pprint(psents[0].productions())

  grammar = parse_pgrammar("""
      # Grammatical productions.
      S -> NP VP [0.99] | VP [0.01] 
      NP -> Pro [0.1] | Det N [0.3] | N [0.5] | NP PP [0.1]
      VP -> Vi [0.05] | Vt NP [0.65] | VP PP [0.05] | VP VP [0.1] | Vt PP [0.1] | Vt Pro_obj NP [0.05]
      Det -> Art [1.0]
      PP -> Prep [0.5]| Prep Pro_obj [0.1] | Prep N [0.38] | Prep Det N [0.01]| Prep Det Pro_obj  [0.01]
     
    # Lexical productions.
      Pro -> "i" [0.1] | "we" [0.1] | "you" [0.1] | "he" [0.3] | "she" [0.2] | "I" [0.2]
      Pro_obj -> "him" [0.3] | "her" [0.3] | "them" [0.4] 
      Art -> "a" [0.4] | "an" [0.1] | "the" [0.5]
      Prep -> "with" [0.3] | "in" [0.3] | "to" [0.4]
      N -> "salad" [0.3] | "fork" [0.3] | "mushrooms" [0.3] | "book" [0.1]
      Vi -> "sneezed" [0.4] | "ran" [0.4] | "was" [0.2]
      Vt -> "eat" [0.2] | "eats" [0.2] | "ate" [0.2] | "see" [0.2] | "saw" [0.1] | "read" [0.1] 
      """)
 
  sentence1 = "he ate salad"
  sentence2 = "he ate salad with mushrooms"
  sentence3 = "he ate salad with a fork"

  # Un-comment the following 2 non-comment lines
  # when working on `PCFG Parser` section in the lab.
  ## Initialize a parser with our toy probabilistic grammar
  ##  (it will have 'S' as the start symbol),
  ##  and parse a sentence
  sppc=BetterICP(grammar)

  for sentence in read_from_file("hw2_input.txt"):
     print("-------------------------------------------------------")
     print("The sentence:{}".format(sentence))
     sppc.parse(sentence.split())
     print("-------------------------------------------------------")
     
 
  # sppc.parse(sentence1.split())
  # # Parse some more complex sentences
  # sppc.parse(sentence2.split())
  # sppc.parse(sentence3.split())

  # prods = get_costed_productions(psents)
  # ppg=PCFG(Nonterminal('NP'), prods)
  # ppc=BetterICP(ppg,1000)
  # # write_line_to_file ("hw2_output.txt" ,"beam = 1000")
  # ppc.parse("the men".split(),True,3)
  # ppc.beam(1075)
  # write_line_to_file ("hw2_output.txt" ,"beam = 1075")
  # ppc.parse("the men".split(),True,3)
  # ppc.trace(3)
  # ppc.beam(1200)
  # write_line_to_file ("hw2_output.txt" ,"beam = 1200")
  # ppc.parse("the men".split(),True,3)

if __name__ == "__main__":
  main()