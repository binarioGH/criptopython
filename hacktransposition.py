#-*-coding: utf-8-*-
from lib.pyperclip import copy
from english import isEnglish 
from transposition_cipher import decode
from platform import python_version as pv 

 
def main():
	if pv()[0] == "3":
		raw_input = input
	message = "Coe nsononnioomm sst mmse  co"
	for key in range(1, len(message)):
		print("Trying with key number {}.".format(key))
		decoded = decode(message, key)
		if isEnglish(decoded):
			ask = raw_input("Is this English?:\n{}\n[yes] [no]>>".format(decoded[:100]))
			if ask == "yes":
				return decoded
	return False

if __name__ == '__main__':
	message = main()
	if message: 
		print("Encryption hacked correctly.\n{}".format(message))
		copy(message)
	else:
		print("Failed to hack encryption.")
