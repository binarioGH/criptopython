#-*-coding: utf-8-*-
if __name__ == '__main__':
	SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?"
	text = input("Introduce the encoded text: ")
	for key in range(len(SYMBOLS)):
		translated = ""
		for symbol in text:
			
			if symbol in SYMBOLS:
				index = SYMBOLS.find(symbol)
				translated += SYMBOLS[index - key]
			else:
				translated += symbol
		print("-"*80)
		print("key #{}: {}".format(key, translated))

