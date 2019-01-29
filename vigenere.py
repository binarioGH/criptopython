#-*-coding: utf-8-*-
from lib.pyperclip import copy
from optparse import OptionParser as op
from platform import python_version as pv
from sys import argv
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#mañana le sigo con estas
def encode(*a):
	pass
def decode(*b):
	pass
#mañana le sigo
def generatekey(message)
def onepad()
def checkargs(do, i):
	if not do in ("encode", "decode", "onepad"):
		print("{} mode not found.".format(do.title()))
		exit()
	if i == "variable":
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
    message = checkargs(o.do, o.input)
    if o.do == "onepad":
    	unbreakable = onepad(message)
    elif o.do == "encode":
    	encode(message, key)
    else:
    	decode(message, key)

if __name__ == '__main__':
	main()