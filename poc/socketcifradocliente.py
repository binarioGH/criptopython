#-*-coding:utf-8-*-
from socket import *
from cryptography.fernet import Fernet
from sys import argv
from platform import python_version as pv
from threading import * 
def readmsj():
	while True:
		try:
			content = sock.recv(1024)
			token = f.decrypt(content)
			print(token.decode())
		except Exception as e:
			print(e)
if __name__ == '__main__':
	if str(pv())[0] == "3":
		raw_input = input
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect((argv[1], int(argv[2])))
	if len(argv) != 4:
		key = Fernet.generate_key()
		print(key.decode())
	else:
		key = argv[3].encode()
	f = Fernet(key)
	reader = Thread(target=readmsj)
	reader.daemon = True
	reader.start()
	msj = " "
	while msj != "exit":
		msj = raw_input(">>>>")
		msj = msj.encode()
		sock.send(f.encrypt(msj))