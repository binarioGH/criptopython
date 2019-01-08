#-*-coding: utf-8
#https://www.nostarch.com/crackingcodes
from lib import pyperclip
from optparse import OptionParser as op
from sys import argv
if __name__ == '__main__':
	SYMBOLS ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?"
	opt = op("Usage: %prog [flag] [value]")
	opt.add_option("-d", "--do",dest="do",default="encode", help="if de value is diferent to 'encode', it decodes.")
	opt.add_option("-k", "--key",dest="key",default=3,help="set key", type="int")
	(o, argv) = opt.parse_args()
	text = input("Input your text: ")
	translated = ""
	for symbol in text:
		if symbol in SYMBOLS:
			symbol_index = SYMBOLS.find(symbol)
			if o.do == "encode":
				translateindex = symbol_index + o.key
			else:
				translateindex = symbol_index - o.key
			if translateindex >= len(SYMBOLS):
				translateindex -= len(SYMBOLS)
			elif translateindex < 0:
				translateindex += len(SYMBOLS)
			translated += SYMBOLS[translateindex]
		else:
			translated += symbol
	print(translated)
	pyperclip.copy(translated)