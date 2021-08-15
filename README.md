# L2_CSR_CPHR - Aref Osman
NCEA L2 Programming & Iterative processes combined asessment 

I created this program using my knowledge on Caesar Cipher encryption.

I thank my computer science teacher Ms Gottschalk (@J-Gottschalk-NZ) for equipping me with this knowledge earlier in the year.


## ***INSTRUCTIONS***


If you haven't used this program before, this section might be of use to understand the purpose of the program and how it works. To use this tool, you will need to have a very basic understanding of Caesar Ciphers. If you are unfamiliar with the concept, I highly recommend visiting this website (https://csfieldguide.org.nz/en/chapters/coding-encryption/substitution-ciphers/) and reading CSFG's article on Caesar Ciphers. This tool can encode/decode a text, with or without a given key. This program ontains an intelligent ""letter frequency analysis tool, that is capable of decoding any text without a given key in the least theoretical possible number of steps. You will be required to enter the following information:
- text (can contain numbers, punctuation etc...)
- a key (if you have one)
- whether you want to encode or decode

## ***ENCRYPTION***

Encryption is an important part of managing data online. It keeps our data safe and secure while being transmitted to the receiver. One way to encrypt data is by using a Caesar Cipher.

A integer between 1-25 (integers out of this range are valid but will have the same effect) is assigned as a key. All letters in the alphabet are shifted by that key.

For example, using a key of 2 will encrypt all letters to the letter 2 intervals ahead, so that 'a' becomes 'c', 'b' becomes 'd' and so on. Letters at the end of the alphabet are pushed to the front. 'y' would become 'a' and 'z' would become 'b'.

Caesar Ciphers are easy to crack, because there are only 25 (26 including the text in its original form) possible permutations to run through.
It is also a two-way encryption method, which means that as opposed to other algorithms such as MD5 or SHA1, texts can be deciphered easily using the same strategy as with encryption (instead using a negative key).


