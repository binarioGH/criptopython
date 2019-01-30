#-*-coding: utf-8-*-
from lib.pyperclip import copy
from optparse import OptionParser as op
from platform import python_version as pv
from sys import argv
from random import choice
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def translate(message, key, mode):
	translated = []
	keyindex = 0
	for symbol in message:
		num = LETTERS.find(symbol.upper())
		if num != -1:
			translated.append(symbol)
		else:
			if mode == "encode":
				num += LETTERS.find(key[keyindex])
			else:
				num -= LETTERS.find(key[keyindex])
			num %= len(LETTERS)	
			if symbol.isupper():
				translated.append(LETTERS[num])
			
			else:
				translated.append(LETTERS[num].lower())

			keyindex += 1
			if keyindex == len(key):
				keyindex = 0
	return "".join(translated)

def validatekey(key):
	for symbol in key:
		if not symbol in LETTERS:
			return False
	return True
def generaekey(message):
	key = ""
	for _ in range(len(message)):
		key += choice(LETTERS)
	return key

def onepad(message):
	key = generatekey()
	return translate(message, key, "encode")
def checkargs(do, i, key):
	if not validatekey(key):
		print("You are using a not valid key.")
		exit()
	if not do in ("encode", "decode", "onepad"):
		print("{} mode not found.".format(do.title()))
		exit()
	if i == "typed":
		message = "Type your message in this variable"
	elif i == "input":
		if pv()[0] == "3":
			raw_input = input
		message = raw_input("Input your text: ")
	else:
		print("{} method not found.".format(i))
		exit()
	return message

def main():
	opt = op("Usage: %prog [args] [values]")
	opt.add_option("-k", "--key",dest="key",help="Set the key.",default="PIZZA")
	opt.add_option("-m", "--mode", dest="do", help="Set what the program is going to do [encode, decode, onepad].",default="encode")
	opt.add_option("-i", "--input", dest="input", help="Set how the data is going to be input [variable, typed].",default="typed")
	(o, argv) = opt.parse_args()
	o.key = o.key.upper()
	message = checkargs(o.do, o.input, o.key)
	if o.do == "onepad":
		translated = onepad(message)
	else:
		translated = translate(message, o.key, o.do)
	print("{}ed message:\n{}\nTranslated message copied in the clipboard.".format(o.do,translated))
	copy(translated)

if __name__ == '__main__':
	main()