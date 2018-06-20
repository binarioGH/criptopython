#!/bin/python3
#-*-coding:utf-8-*-
#solo para linux
import crypt


if __name__ == '__main__':
	word = input("Introduzca una palabra: ")
	salt = input("Introduzca su salt: ")
	password = crypt.crypt(word, salt)
