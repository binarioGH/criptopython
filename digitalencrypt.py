#-*-coding: utf-8-*-
abc = "abcdefghijklmnopqrstuvwxyz"
abc = list(abc)
def main():
	code = [20, 12, 8, 30, 21]
	key = 1939
	print(decode(code, key))
def getkey(message, code):
	abece = "".join(abc)
	key = ""
	for index in range(len(code)):
		key += str(code[index] -  abece.find(message[index]) + 1)
	return int(key)
def decode(code, key):
	key = str(key)
	decoded = ""
	
	count = 0
	for symbol in code:
		symbol -= int(key[count])
		if symbol > len(abc) - 1:
			symbol -= len(abc)
		decoded += abc[symbol - 1] 
		if count >= len(key) - 1:
			count = 0
		else:
			count += 1
	return decoded
if __name__ == '__main__':
	main()