# RE-05 ctfq.exe (120 Points)

This challenge first connects to the server at port:8888 and then send various commands to it.

When we open the binary in IDA we found that at sub_4014A0 it connects to server having ip : 66.42.55.226 and sub_401090 it sends the test command in this format : "id|command|companyname|other"

Initial Idea:
At 1 it sends the command to the server
At 2 it generates the license using some algorithm
At 3 prints "id/command help have been sended to you email"
At 4 Exits

When we enter some random id other than 111 we get an error msg : "wrong id\n id looklike 000-999"

So we need to brute force to get the valid id :
```
ids = [''.join(x) for x in itertools.product(string.digits, repeat=3)]
s.connect(('66.42.55.226',8888))
for i in ids:
	s.send('i|test|test|test\n')
	if "wrong id" not in s.recv(100):
		print i
	print s.recv(50)
print "Done"
s.close()
```
Finally we get valid ids are 111,720.

After giving the valid id it gives another error message : "wrong view command"
So we gave the command as view.

After that it gives another error message : "wrong company"
In problem description we have some company name so after try them we get a valid company : "fis"

After entering all the details we finally get aur license : "vqmuwzjxfmqmdnfhr"

So we have a valid license now we have to reverse the license generator alogrithm to get the secret key.

```
key = 'vqmuwzjxfmqmdnfhr'
co 	= 'fisfisfisfisfisfi'
alpha = string.lowercase
secret = ""
for (k,c) in zip(key,co) :
	diff = ord(k) - ord(c)
	if diff < 0:
		secret += alpha[ord(k) - ord(c)]
	else:
		secret += alpha[ord(k) - ord(c) - 1]
print secret
```

And finally, 
## Our Secret Key : "phuongdonghuyenbi"