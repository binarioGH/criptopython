#-*-coding: utf-8
from rsa import encrypt, decrypt, newkeys
from pyperclip import copy
def main():
	(public, priv) = newkeys(512)

	message = input("Input your message to encrypt: ")
	message += " "
	message = message.encode("latin8")
	encrypted = encrypt(message, public)
	encrypted = encrypted.decode("latin8")
	print("Encrypted message: {}".format(encrypted))
	copy(str(encrypted))
	
	encrypted_message = input("Input your encrypted data: ")
	encrypted_message = encrypted_message.encode("latin8")
	decrypted = decrypt(encrypted_message, priv)
	decrypted = decrypted.decode("latin8")
	print("Decrypted message: {}".format(decrypted))



if __name__ == '__main__':
	main()