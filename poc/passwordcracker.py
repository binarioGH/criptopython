from hashlib import md5
from sys import argv
from optparse import OptionParser as op


if __name__ == '__main__':
	parser = op("Usage: %prog [argument] [value]")
	parser.add_option("-H", "--hash", type="string", help="Set the md5 hash.", dest="hash")
	parser.add_option("-d", "--dictionary", type="string", help="set password dictionary.", dest="dic")
	(opt, argv[1:]) = parser.parse_args()
	try:
		with open(opt.dic, "r") as d:
			for line in d.readlines():
				line = line.strip()
				rt = md5(line.encode()).hexdigest()
				if rt == opt.hash:
					print("{} is {}".format(opt.hash, line))
					break
	except Exception as e:
		print(e)