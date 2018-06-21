#-*-coding:utf-8-*-

def cifrar(cadena, clave, abc):
	text_cifrar = str()
	count = 0
	for letra in cadena:
			suma = abc.find(letra) + abc.find(clave[count] % len(clave))
			modulo = int(suma) % len(abc)
			text_cifrar += str(abc[modulo])
			i += 1
	return text_cifrar
def decif(cadena, clave, abc):
	text_cifrar = str()
	count = 0
	for letra in cadena:
			suma = abc.find(letra) - abc.find(clave[count] % len(clave))
			modulo = int(suma) % len(abc)
			text_cifrar += str(abc[modulo])
			i += 1
	return text_cifrar



if __name__ == '__main__':
	abc = "abcdefghijklmnopqrstuvwxyz"
	c = input("Ingtroduzca la cadena a cifrar: ").lower()
	clave = input("Ingrese su clave: ").lower()
	cif = cifrar(c,clave, abc)
	decif = decif(c,clave,abc)
	print("Cifrado es: {}\nDecifrado es: {}".format(decif))

