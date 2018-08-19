import sys
import os
import hashlib

i = 0
while(i < 99999999):
        val = '{}:{}'.format("b4ckd00r_us3r", i)
        key = hashlib.sha256(val).hexdigest()
        if key == '34c05015de48ef10309963543b4a347b5d3d20bbe2ed462cf226b1cc8fff222e':
            print 'Congr4ts, you found the b@ckd00r. The fl4g is simply : {}:{}'.format("b4ckd00r_us3r", i)
        i = i + 1
