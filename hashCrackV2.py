import hashlib as hb
from os import system
system('clear')

print('  _               _      _____                _   ')
print(' | |             | |    / ____|              | |   ')
print(' | |__   __ _ ___| |__ | |     _ __ __ _  ___| | __')
print(" | '_ \ / _` / __| '_ \| |    | '__/ _` |/ __| |/ /")
print(' | | | | (_| \__ \ | | | |____| | | (_| | (__|   <')
print(" |_| |_|\__,_|___/_| |_|\_____|_|  \__,_|\___|_|\_\'version 2.0")
print('='*70)
print('Author~≥ King')
print('—'*40)

print('Instagram~≥ hacking_with_king')
print('Github~≥ KING3140')
print('—'*40)

print('='*70)

hash=input('Enter the hash to crack:~# ')
wordlist=input('Enter the path of wordlist:~# ')
c=0
try:
	wordlist=open(wordlist,'r')
	quit()
except:
	print('File not found')
for paswd in wordlist:
	hash_obj_1=hb.shake_128(paswd.strip().encode('utf-8')).hexdigest(1)
	hash_obj_2=hb.sha384(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_3=hb.sha256(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_4=hb.sha3_384(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_5=hb.blake2b(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_6=hb.sha224(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_7=hb.sha3_224(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_8=hb.blake2s(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_9=hb.sha3_256(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_10=hb.sha3_512(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_11=hb.sha1(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_12=hb.sha512(paswd.strip().encode('utf-8')).hexdigest()
	hash_obj_13=hb.shake_256(paswd.strip().encode('utf-8')).hexdigest(1)
	hash_obj_14=hb.md5(paswd.strip().encode('utf-8')).hexdigest()
	if hash==hash_obj_1 or hash==hash_obj_2 or hash==hash_obj_3 or hash==hash_obj_4 or hash==hash_obj_5 or hash==hash_obj_6 or hash==hash_obj_7 or hash==hash_obj_8 or hash==hash_obj_9 or hash==hash_obj_10 or hash==hash_obj_11 or hash==hash_obj_12 or hash==hash_obj_13 or hash==hash_obj_14:
		system('clear')
		print('Password found --------> '+paswd)
		c=c+1
	else:
		print('Trying password --------> '+paswd)
if c>1:
	print('Password not match')
