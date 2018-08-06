import bcrypt;
import base64;
import hashlib;
password = "super secret password"
 # Hash a password for the first time, with a randomly-generated salt
hashed = bcrypt.hashpw(
   base64.b64encode(hashlib.sha256(password).digest()),
   bcrypt.gensalt()
 )
 # Check that an unhashed password matches one that has previously been
 # hashed
if bcrypt.checkpw(password, hashed):
     print("It Matches!")
else:
     print("It Does not Match :(")