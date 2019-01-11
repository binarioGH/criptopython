#-*-coding: utf-8-*-
from lib import pyperclip
from sys import argv
from platform import python_version as pv
def main():
	try:
		mykey = argv[2]
	except IndexError:
		mykey = 4

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