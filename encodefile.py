#-*-coding: utf-8-*-
from os import path
from transposition_cipher import encode, decode
from optparse import OptionParser as op
from sys import argv
def main():
	opt = op("Usage: %prog [arg] [value]")
	opt.add_option("-f", "--file",dest="file", default="encodeme.txt", help="Set the name of the file", type="string")
	opt.add_option("-k", "--key",dest="key", default=8, help="Set key", type="int")
	opt.add_option("-o", "--out",dest="out", default="newfile.txt",help="Set output's file name", type="string")
	opt.add_option("-d", "--do", dest="do", default="e", help="Just give a random value tu decode, if not it is going to encode.")
	(o, argv) = opt.parse_args()
	check = encodefile(o.file, o.key, o.out, o.do)
	if check:
		print("Well done, output file in {}".format(o.out))
	else:
		print("There was an execution exception...")

def encodefile(file, key, output, do):
	if path.exists(file):
		if not path.exists(output):
			with open(file) as f:
				content = f.read()
			if do == "e":
				d = encode
			else:
				d = decode
			with open(output, "w") as of:
				of.write(d(content, key))
			return True
		else:
			print("Output file already exist")
			return False
	else:
		print("{} do not exist".format(file))
		return False


if __name__ == '__main__':
	main()