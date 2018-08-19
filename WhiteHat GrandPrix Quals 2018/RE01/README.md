# RE-01 WhiteHat.exe (100 Points)

This challenge is pretty straight forward asks for a key and gives us a flag. So I analyze the binary using IDA and found that at sub_40138F all the exciting stuff goes on.

Overall Key Verification idea is :

```
first_xor = []
for v,k in zip(val,key):
	if (val.index(v) % 2):
		first_xor.append(chr(ord(v) ^ ord(k)))
	else:
		first_xor.append(chr(ord(v)))

add_and_xor = []
for k,f in zip(key,first_xor):
	add_and_xor.append(chr((ord(k) + ord(f)) ^ day))

second_xor = [chr(year ^ ord(v)) for v in first_xor]
```

This verification is defeated to get the key in this way :

```
rev_first_xor = [chr(year ^ f ^ ord(v)) for f,v in zip(final,val)]

for i in range(len(val)):
	if i % 2 == 0:
		rev_first_xor[i] = val[i]

key = "".join([i for i in rev_first_xor])
```

After entering the correct key. The executable drop two files named 2.exe and b.dll in %temp% folder (sub_40111D) and runs the 2.exe using CreateProcessA with "564" as CLA.

After analyzing 2.exe we see that it checks for the parent process ID and must be named to "WhiteHat" if this so it drops the flag.dll in %temp% folder.

But wait this flag.dll is not actually a PE file. By seeing it's header we get that it is an PNG file. By changing the extension to .png we get our flag.

## FLAG : today is good day