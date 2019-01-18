#-*-coding: utf-8-*-
from socket import *
from cryptography.fernet import Fernet as fern
from optparse import OptionParser as op 
from sys import argv
from threading import Thread
from platform import python_version as pv

class Client:
	def __init__(self):
		pass
	def start(self, ip, port, key):
		self.f = fern(key)
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.connect((ip, port))
	def hear(self):
		while True:
			msj = self.sock.recv(1024)
			msj = self.f.decrypt(msj)
			print(msj.decode())
	def send(self, m):
		msj = self.f.encrypt(m.encode())
		self.sock.send(msj)


def main():
	opt = op("Usage: %prog [args] [values]")
	opt.add_option("-s", "--server", dest="server", help="Set server's ip", default="127.0.0.1")
	opt.add_option("-p", "--port", dest="port", help="Set server's port", default=5000, type="int")
	opt.add_option("-k", "--key", dest="key", help="Set key", default="YxqChramWzhDUQiNoAnNseAYTblCjapnL8aQu3ehofQ=")
	(o, argv) = opt.parse_args()
	o.key = o.key.encode()
	c = Client()
	c.start(o.server, o.port, o.key)
	h = Thread(target=c.hear)
	h.daemon = True
	h.start()
	if pv()[0] == "3":
		raw_input = input 
	cmd = ""
	while cmd != "exit":
		cmd = raw_input(">>>")
		c.send(cmd)
if __name__ == '__main__':
	main()