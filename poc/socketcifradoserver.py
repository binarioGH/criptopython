#-*-coding: utf-8-*-
from socket import * 
from sys import argv
from platform import python_version as pv
from os import system, chdir, getcwd
from threading import * 
class Server:
	def __init__(self, ip, port, listen):
		if str(pv())[0] == "3":
			print("Python 3 detectado, creando compatibilidad")
			raw_input = input

		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((ip, int(port)))
		self.sock.listen(int(listen))
		self.sock.setblocking(False)
		self.connections = []
		esperar = Thread(target=self.waitothers)
		leer = Thread(target=self.reader)
		esperar.daemon = True
		leer.daemon = True
		esperar.start()
		leer.start()
		cmd = ""
		while cmd != "exit":
			cmd = raw_input("{}>".format(getcwd()))
			try:
				if cmd[:2] == "cd":
					chdir(cmd[3:])
				else:
					system(cmd)
			except Exception as e:
				print(e)
	def waitothers(self):
		print("Esperando a otros...")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.connections.append(conn)
			except:
				pass

	def sendall(self, msg, cliente):
		print("Mandando mensaje a todos...")
		while True:
			for c in self.connections:
				try:
					if c != cliente:
						c.send(msg)
				except Exception as e:
					self.connections.remove(c)
					print("Sendall: {}".format(e))
	def reader(self):
		print("Leyendo...")
		while True:
			for c in self.connections:
				try:
					m = c.recv(1024)
					sendall(m, cliente)
				except Exception as e:
					print("Reader: {}".format(e))

if __name__ == '__main__':
    m = Server(argv[1], argv[2], argv[3])
	