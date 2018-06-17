#!/usr/bin/python
#-*-coding: utf-8-*-
from sys import argv

def cyph(key, word, alpha):
	deciphword = str()
	for letter in word:
		count = 0
		for l in alpha:
			if letter == " ":
			    deciphword += " "
			    break
			elif letter == l:
				deciphword += alpha[count - key]
			count += 1
	return deciphword



def h():
	print("Opciones de {}:".format(argv[0]))
	print("-k:\nSe usa para establecer la llave del cifrado cesar.")
	print("-w:\nSe usa cuando solo se quiere cifrar una palabra.")
	print("-wrds:\nSe usa cuando se quiere cifrar una frase.\nUso:")
	print("{} -key (numero) -wrds\nNo es necesario poner nada despues de esta bandera.".format(argv[0]))
if __name__ == '__main__':
	alph = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
	if len(argv) == 1:
		print("Usa {} -h para ver las opciones")
		exit()
	else:
		key = 0
		word = ""
		argcount = 0 
		count = 0
		for arg in argv:
			if arg[0] != "-":
				argcount += 1
				continue
			elif arg == "-h":
				h()
				exit()
			elif arg == "-w":
				word = argv[argcount + 1]
				count += 1
			elif arg == "-wrds":
				word = raw_input("Introduce aquí lo que quieres cifrar: ")
				count += 1
			elif arg == "-k":
				try:
					key = int(argv[argcount + 1])
				except:
					print("{} no es un numero entero.".format(argv[argcount + 1]))
					exit()
			argcount += 1
			if count > 1:
				print("No se puede usar -wrds y -w al mismo tiempo.")
				exit()
		if word != "" and key != 0:
			cph = cyph(key, word, alph)
			print("'{}' cifrado es:\n{}".format(word, cph))
		else:
			print("Usa {} -h para ver las opciones.".format(argv[0]))

 