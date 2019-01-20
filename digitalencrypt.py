#-*-coding: utf-8-*-

def main():
	code = [20, 12, 18, 30, 21]
	key = 1939
	print(decode(code, key))
def decode(code, key):
	key = str(key)
	decoded = ""
	abc = "abcdefghijklmnopqrstuvwxyz"
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