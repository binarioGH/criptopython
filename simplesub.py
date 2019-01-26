#-*-coding: utf-8-*-
from lib.pyperclip import copy
from random import shuffle
from optparse import OptionParser as op
from sys import argv
from platform import python_version as pv
LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  	

def main():
	opt = op("Usage: %prog [args] [values]")
	opt.add_option("-k", "--key",dest="key", help="Set key", default="CXNQWSUJLYBOZAPRHIMGDVTFEK")
	opt.add_option("-i", "--input",dest="input" , help="Set if you are going to input the message manually ir not. [input, variable]", default="manually")
	opt.add_option("-d", "--do", dest="do", help="Set what the programm is going to do [decode, encode, generatekey]", default="encode")
	(o, args) = opt.parse_args()
	message = checkargs(o.key,o.do, o.input)
	if o.do != "generatekey":
		translated = sub(message, o.key, o.do)
		print("The {}ed message is:\n {}\nThe message was copy in the clipboard.".format(o.do, translated))
		copy(translated)
	else:
		newkey = getkey()
		print("New key: {}\nThe key was copy in the clipboard".format(newkey))
		copy(newkey)
def checkargs(key, do, inp ):
	if not len(key) == len(LETTERS):
		print("{} is not a valid key.".format(key))
		exit()
	if not do in ("encode", "decode", "generatekey"):
		print("'{}' mode not found".format(do))
		exit()
	if not do == "generatekey":
		if inp == "manually":
			if pv()[0] == "3":
				raw_input = input
			text = raw_input("Input your text: ")
		elif inp == "variable":
			text = "Input your text here"
		return text


def sub(msj, key, mode):
	abc = "".join(LETTERS)
	translated = ""
	if mode == "decode":
		abc, key = key, abc
	for symbol in msj: 
		if symbol.isupper():
			translated += key[abc.find(symbol)]
		elif symbol.islower():
			translated += key[abc.find(symbol.upper())].lower()
		else:
			translated += symbol
	return translated


	
def getkey():
	symbols = "".join(LETTERS)
	symbols= list(symbols)
	shuffle(symbols)
	return "".join(symbols)

if __name__ == '__main__':
	main()