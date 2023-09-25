# //infosys dsa question count the words in a string
from os import *
from sys import *
from collections import *
from math import *


from sys import stdin
string = input()

def countWords(string) :
	# Your code goes here
    space= string.count(" ")
    totalWords = space+1
    return totalWords
words = countWords(string);
print(words)

	


