import bcrypt;
import base64;
import hashlib;
import random;
from array import *;
def testPass(cryptedPass):
		salt = cryptedPass[0:2]
		dictFile = open('dictionary.txt')
		for word in dictFile.readlines():
				word = word.strip('\n')
				cryptWord = bcrypt.checkpw(word, cryptedPass)
				if(cryptWord):
 					print ("[+] Found Password: " + word + "\n");
 					return
		print("[-] Password Not Found.\n")
		return

def main():
		f = open('list.txt')
		for line in f.readlines():
				print('///010101 Cracking: ' + line)
				testPass(line)
if __name__ == "__main__":
	main()


