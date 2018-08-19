val = "abcdefghiklmopqx"
#key = aycnemg islKoaqh

final = [0x83,0xf9,0x81,0xe8,0x87,0xe9,0x85,0xaa,0x8b,0xfa,0x8e,0xc4,0x8d,0xf3,0x93,0xf2]
day = 0x12
year = 0xe2


'''
#Key Verifier

first_xor = []
for v,k in zip(val,key):
	if (val.index(v) % 2):
		first_xor.append(chr(ord(v) ^ ord(k)))
	else:
		first_xor.append(chr(ord(v)))
print "First XOR : "
print first_xor

add_and_xor = []
for k,f in zip(key,first_xor):
	add_and_xor.append(chr((ord(k) + ord(f)) ^ day))
print "Add and XOR : "
print add_and_xor

second_xor = [chr(year ^ ord(v)) for v in first_xor]
print "Second XOR"
print second_xor

'''

# Getting the key
rev_first_xor = [chr(year ^ f ^ ord(v)) for f,v in zip(final,val)]

for i in range(len(val)):
	if i % 2 == 0:
		rev_first_xor[i] = val[i]

key = "".join([i for i in rev_first_xor])
print "Key : " + key