from PyDictionary import PyDictionary
import sys

dictionary=PyDictionary()
word = sys.argv[1] #takes cli argument as string variable

print (dictionary.meaning(word))