#-*-coding: utf-8-*-
from socket import *
from threading import *
from platform import python_version as pv
from platform import platform
from os import system, chdir, getcwd
class Server():
	def __init__(self):
		self.users = []
		cmd = ""
		if str(pv())[0] == "3":
			raw_input = input
		if str(platform())[0] == "W":
			clear = "cls"
		else:
			clear = "clear"
		self.accept_connections = True
		self.send2all = True
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind(("0.0.0.0", 5000))
		self.sock.listen(4)
		self.sock.setblocking(False)
		esperar = Thread(target=self.connect)
		esperar.daemon = True
		esperar.start()
		escuchar = Thread(target=self.hearall)
		escuchar.daemon = True
		escuchar.start()
		while cmd != "exit":
			try:
				cmd = raw_input("{}-->".format(getcwd(	)))
				if cmd[:2] == "cd":
					chdir(cmd[3:])
				elif cmd == clear:
					system(clear)
				elif cmd[:4] == "stop":
					if cmd[5:] == "connect":
						self.accept_connections = False
					elif cmd[5:] == "hearall":
						self.send2all = False
				else:
					print("Comando no reconocido.")
			except Exception as e:
				print(e)
		self.sock.shutdown(SHUT_RDWR)
		self.sock.close()
	def connect(self):
		while self.accept_connections:
			try:
				conn = self.sock.accept()[0]
				conn.setblocking(False)
			except:
				pass
	def hearall(self):
		while self.send2all:
			try:
				for ip in self.users:
					recv = ip.recv(1024)
					if recv:
						self.sendall(recv, ip)
			except:
				pass
	def sendall(self, msg, sndr):
		for ip in self.users:
			if ip == sndr:
				continue
			else:
				try:
					ip.send(msg)
				except:
					print("{} se ha desconectado.".format(ip))
					self.users.remove(ip)
if __name__ == '__main__':
	main = Server()