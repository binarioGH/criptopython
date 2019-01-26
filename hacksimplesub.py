#-*-coding: utf-8-*-
from lib.pyperclip import copy
from optparse import OptionParser as op 
from simplesub import sub as decode
from english import isEnglish 
from sys import argv
PATTERNS = {}
def main():
	opt = op("Usage: %prog [args] [values]")
	opt.add_option("-d", "--dic",dest="dic",default="dic.txt",help="Set diccionary file")
	(o, argv) = opt.parse_args()
	loaddic(o.dic)
	translated = 
def loaddic(dic):
	file = open(dic, "r")
	for word in file.read().split("\n"):
		pattern = detectpattern(word)
		if pattern not in PATTERNS:
			PATTERNS[pattern] = []
		PATTERNS[pattern].append(word)
	file.close()
def detectpattern(word):
	pattern = []
	for letter in word:
		index = str(word.find(letter))
		pattern.append(index)
	return ".".join(pattern)



if __name__ == '__main__':
	main()