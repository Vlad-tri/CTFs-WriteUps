# RE-03 DebugMe.exe (380 Points)

This binary simple asks for the key and we have to reverse its key validating algorithm.

When we first load the binary in the debugger it runs its just terminate due to some anti-debug checks. But I am not bother about this right now. I simply runs the executable and then attach the debugger the the process.

#### [Note] : I also attach my .idb file having some renames and comments while analyzing this binary. I recommend to use this while reading this writeup.

When we load the executable in IDA we saw that at sub_4029C0 the validation process goes on. Let's dive into this.

At 00402A73 it calls surely_part_checker (sub_402BB0). Then at 00402BB0 it checks that key length should be greater than or equals 10.

If we provide 10 length key then,
* At 00402CBD it calls add_3_first_9_r (sub_404010) - means add 3 to 0-9 elements and set last as r
* But when at 00402CE0 when it calls simple_copy_11_19_r (sub_404100) - means simple copy 11-19 and set last as r, it throws an error box.

So we need to provide the key of length 20 now.
When we provide 20 length key then,
* At 00402DC0 it calls add_3_first_9_r
* At 00402DE3 it calls simple_copy_11_19_r
* But when at 00402E06 when it calls add_5_21_29_f (sub_404200) - means add 5 to 21-29 and set last as f, it throws an error box.

So now we need to provide the key of length 30 now.
When we provide 30 length key then,
* At 00402EFF it compares the key length with 40 and throws an error box.

So now we need to provide the key of length 40 and then checks the last element must be 'x'.
When we provide 40 length key then,
* At 00402F3F it calls add_3_first_9_r
* At 00402F62 it calls simple_copy_11_19_r
* At 00402F85 it calls add_5_21_29_f
* At 00402FA8 it calls add_3_b_32_39_r - means set b first and the from 32-39 add 3 and set last as r
* At 00402FCB it calls add_3_0_19_r (sub_404420)(I think you get it now.... ༽(•⌣•)༼ )
* At 00402FEE it calls add_3_21_39_r (sub_404510)
* At 00403011 it calls add_2_11_29_r (sub_404620)

At 00403032 it calls add_2_and_3_0_9_r_on_add_3_first_9_r (sub_403420) which adds 2 and 3 alternatively on output from add_3_first_9_r and then compares it with "poskjyrvyr". 

If this checks succeeds then,
* At 004030B8 it calls add_9_and_5_11_19_r_on_simple_copy (starting with 9 and add it on every 4th index and remaining with 5)
* At 004030F0 it calls sub_404970 which compares results with "j676kn|5nr".

If this check succeeds then,
* At 00403112 it calls add_3_and_1_21_29_f_on_add_5 (sub_403790) (starting with 3 and add it on every 3rd index and remaining with 1)
* At 0040314A it calls sub_404970 which compares results with "uku|nokxqf"

If this check succeeds then,
* At 0040316C it calls sub_403940 (starting with 2 and add it on every 2nd index and remaining with 1)
* At 004031EC it calls sub_404970 which compares results with "dzihggh{er"

And in the same sense it checks on other section. This is the whole main idea behind this key verifier.

For the whole solution check out the python script.

