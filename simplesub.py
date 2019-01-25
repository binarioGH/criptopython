#-*-coding: utf-8-*-
from lib.pyperclip import copy
from random import shuffle
from optparse import OptionParser as op
from sys import argv
from platform import python_version as pv
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def main():
	opt = op("Usage: %prog [args] [values]")
	opt.add_option("-k", "--key",dest="key", help="Set key", default="CXNQWSUJLYBOZAPRHIMGDVTFEK")
	opt.add_option("-i", "--input",dest="input" , help="Set if you are going to input the message manually ir not. [input, variable]", default="manually")
	opt.add_option("-d", "--do", dest="do", help="Set what the programm is going to do [decode, encode]")
	(o, args) = opt.parse_args()
	checkargs(o.key,o.do, o.input)
	
def checkargs(key, do, inp ):
	if not list(key).sort() == LETTERS:
		print("{} is not a valid key.".format(key))
		exit()
	if not do in ("encode", "decode"):
		print("'{}' mode not found".format(do))
		exit()
	
def getkey()
	symbols = "".join(LETTERS)
	symbols= list(symbols)
	shuffle(symbols)
	return "".join(symbols)

if __name__ == '__main__':
	main()