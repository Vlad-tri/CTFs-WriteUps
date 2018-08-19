<h1>Description</h1>

<h3>Problem Statement</h3>
The smart home system has the function of remote monitoring of what is happening in the home and every few minutes sends pictures 
of the surveillance cameras to the owner of the house. You successfully intercepted the network traffic of this system, however, 
its creators took care of the security of their users data and encrypted the pictures. 
Decrypt the provided image and you will find the flag.

<h3>Problem Tag: Crypto</h3>

<h3>Solution</h3>
This problem is very simple at first sight the given image looks like PNG but it is not (maybe encrypted). So we check for the
encryption by comparing this given with another PNG image on hexeditor.
After stucking for sometime we got that it is the simple XOR operation by XOR the original PNG header values with encrypted header
values and get a constant value 255. So XORing all data with 255(0xff) we get our decrypted image.
