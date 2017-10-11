import binascii
import re

with open("secret_encrypted.png","rb") as fr: data = fr.read()
data = data.encode("hex")
data_mod = re.findall("..",data)
data_out = []
for i in data_mod:
    data_out.append(chr(int(i,16) ^ 255))
data_mod_out =  "".join(data_out)
with open("res.png","wb") as fw : fw.write(data_mod_out)


