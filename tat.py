#-*-coding: utf-8-*-
from sys import argv
from itertools import combinations
from time import strftime
'''There is a popular post on instagram that says 'how old are you?'
and you have to add years based on what things have you done.
i want to crack what things have they done.
'''

THINGS = {
	"Gave head": 4,
	"Received head": 2,
	"Got fingered": 3,
	"Fingered someone": 3,
	"Gave hickey": 1,
	"Received hickey": 3,
	"Sent nudes": 1,
	"Kissed on sb neck": 3,
	"Dry hump": 5,
	"Had sex": 10,
	"Sex tape": 7,
	"Had car sex": 15,
	"Fucked in your house": 9,
	"Fucked yo gf/bf": 8,
	"Fucked sb you wasn't with": 6,
	"Cheated": 8,
	"Sent traps": 4,
	"Catfished sb": 6,
	"Got titties sucked": 3,
	"Sucked titties": 2,
	"Got handjob": 9,
	"Tongue kissed": 2,
	"Did something in the elevator": 4,
	"Did something in the stairs": 3,
	"Sucked toes": 6 #wtf
}

def main():
	if len(argv) == 1:
		total = int(input("How many years? "))
	else:
		try:
			total = int(argv[1])
		except:
			total = int(input("How many years? "))
	answares = []
	for num in range(1, len(THINGS)):
		print("Combinations: {}".format(num))
		for i in combinations(THINGS, num):
			jtotal = 0
			for j in i:
				jtotal += THINGS[j]
			if jtotal == total:
				answare = ", ".join(i)
				answares.append(answare)

	print("\n"*20)
	print("Starting to write file.")
	filename = "{}.txt".format(strftime("%d-%m-%y-%H-%M-%S"))
	with open(filename , "w") as f:
		for answare in answares:
			f.write("{}\n".format(answare))


if __name__ == '__main__':
	main()