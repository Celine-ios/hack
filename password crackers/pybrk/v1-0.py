import bcrypt;
import base64;
import hashlib;
import random;
from array import *;

pwList = ['wsasas', 'word', 'super secret password']
password = "super secret password".encode('utf-8')
 # Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(
#base64.b64encode(hashlib.sha256('super secret password'.encode('utf-8')).digest())
'super secret password'.encode('utf-8'),
bcrypt.gensalt()
)
 # Check that an unhashed password matches one that has previously been
 # hashed
i = 0
while not bcrypt.checkpw(pwList[i].encode('utf-8'), hashed):
	#if bcrypt.checkpw(password, hashed):
    #	 print("It Matches!")
	#else:
    print("It Does not Match :(")
    i = i + 1

print('It matches, damn!, Password: ' + str(pwList[i]))