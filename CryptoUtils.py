#!/usr/bin/python
import random
import base64
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util import randpool
from Crypto.Util import number
import hashlib


def pad(s):
	while len(s) % 16 != 0:
		s += '\n'#null padding for now
	return s

def removePadding(s):
	return s.rstrip('\n')

def generateIV():
	return hex(int(random.random()*0x10000000000000000) + int(random.random()*0x1000)).strip("0x").strip("L")

def encrypt(algorithm,key,string):
	ciphertext = ""
	if algorithm == "AES":
		ciphertext = AESencrypt(key,string)
	return ciphertext

def decrypt(key,ciphertext):
	components = ciphertext.split(":")
	plaintext = ""
	if components[0] == "AESCBC" or components[0] == "AESCBC":
		plaintext = AESdecrypt(key,components[1],components[2])
	return plaintext

def AESencrypt(K,pt):
	key = pad(K)
	prefix = "AESCBC:"
	iv = pad(generateIV())
	obj = AES.new(key, AES.MODE_CBC,iv)
	ct = obj.encrypt(pad(pt))
	b64 = base64.b64encode(ct)
	return prefix+iv+":"+b64

def AESdecrypt(K,iv,b64):
	key = pad(K)
	try:
		ct = base64.b64decode(b64)
	except TypeError:
		return 'Decryption Error: Invalid characters.  Did you select the wrong operation?'
	if len(ct) % 16 != 0:
		return "Decryption Error: Length doesn't match up"
	obj2 = AES.new(key,AES.MODE_CBC,iv)
	pt = obj2.decrypt(ct)
	return removePadding(pt) 

def makehash(value):
	return "SSH224::"+hashlib.sha224(value).hexdigest()

key = "too many tools in the woodshed"
r =encrypt("AES",key,"anybody up for naked hot tubbing and oil massages later tonight?")
print r, len(r)
print decrypt(key,r)

