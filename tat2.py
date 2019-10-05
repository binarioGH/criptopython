#-*-coding: utf-8-*-
from json import dumps
from sys import argv
from time import strftime
from operator import itemgetter

def sortDic(dic):
	new_dic = {}
	odic = len(dic)
	while len(new_dic) != odic:
		biggest = max(dic.items(), key=itemgetter(1))[0]
		new_dic[biggest] = dic[biggest]
		del dic[biggest]
	return new_dic


		


def main():
	try:
		with open(argv[1], "r") as f :
			content = f.read()
			content = content.split("\n")
	except:
		print("Something went wrong.")
		return 0
	THINGS = {}
	for thing in content:
		things = thing.split(", ")
		for thing in things:
			if thing in THINGS:
				THINGS[thing] += 1
			else:
				THINGS[thing] = 1
	THINGS = sortDic(THINGS)
	jcontent = dumps(THINGS, indent=4)
	filename = "{}.json".format(strftime("%d-%m-%y-%H-%M-%S"))
	with open(filename, "w") as f:
		f.write(jcontent)





if __name__ == '__main__':
	main()