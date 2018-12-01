#-*-coding: utf-8-*-
from socket import *
from threading import *
#para ver si lo que está mal son los clientes que se cifran o el servidor.
def hearing():
	while True:
		recv = sock.recv(1024).decode()
		print(recv)
if __name__ == '__main__':
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(("192.168.2.177", 5111))
	h = Thread(target=hearing)
	h.daemon = True
	h.start()
	msj = ""
	while msj != "exit":
		msj = input(">>>")
		sock.send(msj.encode())