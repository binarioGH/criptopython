#-*-coding: utf-8-*-
from hashlib import * 
from optparse import OptionParser as op
from sys import argv
def gethash(a,i,file):
	if file:
		f = open(i, "rb")
		tohash = f.read()
	else:
		tohash = i
	exec("print({}({}).hexdigest())".format(a,tohash))


if __name__ == '__main__':
	algorithms = algorithms_guaranteed
	opt = op("Usage:%prog [options] [values]")
	opt.add_option("-w", "--word",type="string",help="Set word or to hash",default=None,dest="word")
	opt.add_option("-a","--algorithm",type="string",help="Set algorithm",default="md5",dest="algorithm")
	opt.add_option("-f", "--file",type="string",default="off",help="Set 'on' if you want to get a file's hash, else use'off'",dest="file")
	(o, argv) = opt.parse_args()
	if o.file == "on":
		f = True
	else:
		f = False
	if o.algorithm not in algorithms:
		print("Algorithm '{}' not found.".format(o.algorithm))
		exit()
	gethash(o.algorithm, o.word, f)
