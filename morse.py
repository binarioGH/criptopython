#-*-coding: utf-8-*-

def code(plain_text):
	coded_text = ""
	for char in text:
		if char in abc:
			coded_text += abc[char]
		else:
			coded_text += "*"
	return coded_text
def decode(morse):
	plain_text = ""
	current_seq = ""
	for dot_dash in morse:
		if dot_dash == "/":
			confirm  = True
			for char in abc:
				if "{}/".format(current_seq) == abc[char]:
					plain_text += char
					confirm = False
			if confirm:
				plain_text += "*"
			current_seq = ""
		else:
			current_seq += dot_dash
	return plain_text

if __name__ == '__main__':
	abc = {
	"a": ".-/",
	"b": "-.../",
	"c": "-.-./",
	"d": "-../",
	"e": "./",
	"f": "..--./",
	"g": "--./",
	"h": "..../",
	"i": "../",
	"j": ".---/",
	"k": "-.-/",
	"l": ".-../",
	"m": "--/",
	"n": "-./",
	"o": "---/",
	"p": ".--./",
	"q": "--.-/",
	"r": ".-./",
	"s": ".../",
	"t": "-/",
	"u": "..-/",
	"v": "...-/",
	"x": ".--/",
	"y": "-.--/",
	"z": "--../",
	"1": ".----/",
	"2": "..---/",
	"3": "...--/",
	"4": "....-/",
	"5": "...../",
	"6": "-..../",
	"7": "--.../",
	"8": "---../",
	"9": "----./",
	"0": "-----/",
	" ": "\\/"}
	coded_text = ""
	dorc = ""
	while dorc != "D" and dorc != "C":
		dorc = input("[D] to decode, [C] to code: ")
		dorc = dorc.upper()
	text = input("Enter your text: ")
	text = text.lower()
	if dorc == "D":
		prnt = decode(text)
	else:
		prnt = code(text)
	print(prnt) 

	