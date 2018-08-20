key = ""

s = "poskjyrvyr"
s1 = ""
for i in xrange(9):
	if i % 2 == 0:
		s1 += chr(ord(s[i]) - 2)
	else:
		s1 += chr(ord(s[i]) - 3)

s2 = "".join([chr(ord(x) - 3) for x in s1])
s2 += 'r'
print s2
key += s2

s1 = ""
t = "j676kn|5nr"
for i in xrange(9):
	if i % 5 == 0:
		s1 += chr(ord(t[i]) - 9)
	else:
		s1 += chr(ord(t[i]) - 5)

s2 = "".join([chr(ord(x)) for x in s1])
s2 += 'r'
print s2
key += s2

s1 = ""
u = "uku|nokxqf"
for i in xrange(9):
	if i % 4 == 0:
		s1 += chr(ord(u[i]) - 3)
	else:
		s1 += chr(ord(u[i]) - 1)

s2 = "".join([chr(ord(x) - 5) for x in s1])
s2 += 'f'
print s2
key += s2

s1 = ""
v = "dzihggh{er"
for i in xrange(9):
	if i % 3 == 0:
		s1 += chr(ord(v[i]) - 2)
	else:
		s1 += chr(ord(v[i]) - 1)
s1 = s1[1:]
s2 = "".join([chr(ord(x) - 3) for x in s1])
s2 = 'b'+s2+'x'
print s2
key += s2

s1 = ""
w = '\x90rwn\x8a|vy\x99mj:W:on\x9c9rr'
for i in xrange(19):
	if i % 4 == 0:
		s1 += chr(ord(w[i]) - 0x22)
	else:
		s1 += chr(ord(w[i]) - 6)

s2 = "".join([chr(ord(x) - 3) for x in s1])
s2 += 'r'
print s2

s1 = ""
x = '\x82lv}m~lyplE}ljjxj~hr'
for i in xrange(19):
	if i % 5 == 0:
		s1 += chr(ord(x[i]) - 0x12)
	else:
		s1 += chr(ord(x[i]) - 4)

s3 = "".join([chr(ord(x) - 3) for x in s1])
s3 += 'x'
print s3

s1 = ""
y = 'd343igy2llogrxhkhtkr'
for i in xrange(19):
	if i % 4 == 0:
		s1 += chr(ord(y[i]) - 1)
	else:
		s1 += chr(ord(y[i]))
print s1

s4 = ""
for l in xrange(19):
	s4 += chr(ord(s1[l]) - 2)
s4 += 'e'
print s4

key = s2[:10] + s4 + s3[10:]

print "Key : " + key

# kineesmptra121few0ijmeovfierifbveccccwax