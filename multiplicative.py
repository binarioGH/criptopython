#-*-coding: utf-8-*-
from lib.pyperclip import copy
from math import sqrt
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ABC = ABC + ABC.lower()
ABC +="1234567890 !?."
ABC = list(ABC)
def main():
	message = "iun" #iun	
	key = 17
	mode = "dencode"
	if mode == "encode":
		prnt = encode(message, key)
	else:
		prnt = decode(message, key)

	print(prnt)
	copy(prnt)
def encode(text, key):
	abc = "".join(ABC)
	encoded = ""
	for symbol in text:
		add = abc.find(symbol)  * key
		if add > len(abc):
			add = add%len(abc)
		encoded += abc[add]
	return encoded

def decode(text, key):
	abc = "".join(ABC)
	modularinverse = getmodularinverse(key, len(abc))
	decoded = ""
	for symbol in text:
		add = abc.find(symbol) * modularinverse
		if add > len(abc):
			add = add / len(abc)
		decoded += abc[add]
	return decoded

def getmodularinverse(a, m):
	for i in range(2,int(sqrt(m))):
		if (a * i) % m == 1:
		    return i
	return 1 


if __name__ == '__main__':
	main()