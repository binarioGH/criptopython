#-*-coding: utf-8-*-
from transposition_cipher import encode, decode
from random import randint, seed, shuffle
def main():
	seed(42)
	for i in range(20):
		message = "ABCDEFGHIJKLMNOPKRSTUVWXYZ" * randint(2,10)
		message = list(message)
		shuffle(message)
		message = "".join(message)
		print("Test #{}: {}".format(i + 1, message[:50]))
		for key in range(1, int(len(message) / 2)):
			e = encode(message, key)
			d = decode(e, key)
			if message != d:
				print("Mismatch with key {}.".format(key))
				exit()
	print("Test passed.")
if __name__ == '__main__':
	main()