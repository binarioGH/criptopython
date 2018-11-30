'''#-*-coding: utf-8-*-
from cryptography.fernet import Fernet
from sys import argv

def cifrararchivo(file, clave):
	with open(file, "read"):


if __name__ == '__main__':

	key = ""
	file = ""
	count = 0
	for a in argv:
		if a[0] != "-":
			count += 1
			continue
		elif a == "-f":
			file = argv[count + 1]
		elif a == "-k":
			key = argv[count + 1].encode()
		else:
			print("Parametro {} no encontrado.".format(a))
			exit()
		count += 1
	if key == "":
		key = Fernet.generate_key()

	c = Fernet(key)
	cifrararchivo(file, clave)

'''