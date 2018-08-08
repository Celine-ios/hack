import bcrypt;
import base64;
import hashlib;
import random;
from array import *;

pwList = ['wsasas', 'word', 'super secret password']
i = 0
while  i < len(pwList):
	f = open('list.txt', 'a')
	cryptpw = bcrypt.hashpw(pwList[i].encode('utf-8'), bcrypt.gensalt())
	f.write(str(cryptpw) + "\n")
	i = i + 1
