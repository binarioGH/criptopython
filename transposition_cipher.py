#-*-coding: utf-8-*-
from lib import pyperclip
from sys import argv
from platform import python_version as pv
def main():
	if len(argv) <= 2:
		mykey = 8
	else:
		mykey = argv[1]
	if pv()[0] == "3":
		raw_input = input
	mytext = raw_input("Input your text here: ")
	encoded = encode(mytext, mykey)
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


if __name__ == '__main__':
	main()