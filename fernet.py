#-*-coding:utf-8-*-
from cryptography.fernet import fernet
from sys import argv


if __name__ == '__main__':
	count = 0
	clave = ""
	texto = ""
	crpt = True
	for arg in argv:
		if arg[0] != "-":
			count+=1
			continue
		else:
			if arg == "-key":
				clave = argv[count + 1].encode()
			elif arg == "-text":
				texto = argv[count + 1].encode()
			elif arg == "--decrypt":
				crpt = False
			count += 1
	if clave == "":
		print("[+] Generando clave...")
		clave = Fernet.generate_key()
		print(clave.decode())
	f = Fernet(clave)

	if crpt == True:
		print("[+] Encriptando...")
		token = f.encrypt(texto.encode())
		print(token)
	else:
		print("[+] Desencriptando...")
		des = f.decrypt(texto.encode())
		print(des)
	
	
