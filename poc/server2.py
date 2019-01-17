#-*-coding: utf-8-*-
from socket import *
from optparse import OptionParser as op 
from cryptography.fernet import Fernet as fern 
from sys import argv
from threading import Thread
from platform import python_version as pv
from platform import platform as p
from os import system

class Server:
	def start(self, ip, port, key, listen):
		self.f = fern(key)
		self.l = listen
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.bind((ip, port))
		self.sock.settimeout(0.0)
		self.sock.listen(self.l)
		self.serverstuff = {"wait": True, "printaddr": True, "hear":True}
		self.conns = {}
		self.clientnum = 1
	def wait4all(self):
		while self.serverstuff["wait"]:
			while self.l <= len(self.conns):
				if not self.serverstuff["wait"]:
					break
				try:
					conn, addr = self.sock.accept()
					self.conns["Client-{}".format(self.clientnum)] = conn
					if self.serverstuff["printaddr"]:
						print("{}\nNew connection.\nIP: {}\nPORT: {}\n".format("-"*80,addr[0], addr[1],"-"*80))
				except BlockingIOError:
					pass
				except Exception as e:
					print("Error : {}".format(e))
				else:
					self.clientnum += 1

	def hear2all(self):
		while self.serverstuff["hear"]:
			for c in self.conns:
				try:
					msj = self.conns[c].recv(1024)
					if self.serverstuff["send"]:
						self.sendtoall(msj, c)
				except:
					pass
	def send2all(m, c):
		for client in self.conns:
			if client == c:
				continue
			try:
				self.conns[client].send(m)
			except:
				del self.conns[client]
	def shutdown(self):
		for c in self.conns:
			self.conns[c].shutdown(SHUT_WR)
			self.conns[c].close()
		for stuff in self.serverstuff:
			self.serverstuff[stuff] = False
		self.sock.close()

def main():
	opt = op("Usage: %prog [arg] [value]")
	opt.add_option("-H","--host",dest="host",default="127.0.0.1", help="Set server's ip")
	opt.add_option("-p", "--port", dest="port", default=5000, help="Set server's port", type="int")
	opt.add_option("-k", "--key", dest="key", default="YxqChramWzhDUQiNoAnNseAYTblCjapnL8aQu3ehofQ=", help="Set key", type="string")
	opt.add_option("-l", "--listen", dest="l", default=2, help="Set how many clients can be connected at the same time", type="int")
	(o, argv) = opt.parse_args()
	s = Server()
	s.start(o.host, o.port, o.key, o.l)
	w = Thread(target=s.wait4all)
	w.daemon = True
	w.start()
	h = Thread(target=s.hear2all)
	h.daemon = True
	h.start()
	if pv()[0] == "3":
		raw_input = input
	if p()[0] == "W":
		clear = "cls"
	else:
		clear = "clear"
	costumclear = clear
	cmd = ""
	while cmd != "exit":
		cmd = raw_input(">>>")
		if cmd == costumclear:
			system(clear)




if __name__ == '__main__':
	main()