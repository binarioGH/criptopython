#-*-coding: utf-8-*-
from lib import pyperclip
from sys import argv
from platform import python_version as pv
from optparse import OptionParser as op
from math import ceil
def main():
	opt = op("Usage: %prog [args] [values]")
	opt.add_option("-k", "--key", dest="key",help="Set key.",default=4,type="int")
	opt.add_option("-d", "--do", dest="do", help="If this argument is equal to its default value ('encode') it will encode your text, else, it will decode it.",default="encode")
	(o, argv) = opt.parse_args()
	if pv()[0] == "3":
		raw_input = input
	mytext = raw_input("Input your text here: ")
	if o.do == "encode":
		encoded = encode(mytext, o.key)
	else:
		encoded = decode(mytext,o.key)
	print(encoded)
	pyperclip.copy(encoded)

def encode(text, key):
	ciphertext = [''] * key
	for column in range(key):
		currentindex = column 
		while currentindex < len(text):
			ciphertext[column] += text[currentindex]
			currentindex += key
	return ''.join(ciphertext)
def decode(text, key):
	numofcolumns = int(ceil(len(text)/float(key)))
	numofrows = key
	numofshadeboxes = (numofcolumns * numofrows) - len(text)
	plaintext = [''] * numofcolumns 
	row = 0
	column = 0
	for symbol in text:
		plaintext[column] += symbol
		column += 1
		if (column == numofcolumns) or (column == numofcolumns -1 and row >= numofrows  - numofshadeboxes):
			column = 0
			row += 1
	return ''.join(plaintext)

if __name__ == '__main__':
	main()