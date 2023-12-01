## level09

```bash
$ su level09 25749xKZ8L7DkSCwJkT9dyv6f
```

### Vulnerability Assessment

```bash
$ ./level09 
You need to provied only one arg.
```

The directory contains two files: an executable named `level09` and a file named `token`. The contents of the `token` file appear to be encoded or obfuscated. Running the `level09` program suggests it manipulates strings based on the index of each character.

```bash
level09@SnowCrash:~$ cat token 
f4kmm6p|=�p�n��DB�Du{��
```

```bash
$ ./level09 ""

$ ./level09 "a"
a
$ ./level09 "aa"
ab
$ ./level09 "aaa"
abc
$./level09 0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~�����������
```

The `level09` program alters each character in a string by adding its index in the string to its ASCII value:

```bash
ASCII  | DEC | CALCUL | AFTER  | DEC after
	97   |  a  | a + 0  | 98     | a
	98   |  b  | b + 1  | 99     | c
	99   |  c  | c + 2  | 101    | e
	100  |  d  | d + 2  | 103    | g
	101  |  e  | e + 3  | 104    | i
	102  |  f  | f + 4  | 106    | k
	103  |  g  | g + 5  | 108    | m
	104  |  h  | h + 6  | 110    | o
	105  |  i  | i + 7  | 112    | q
	106  |  j  | j + 8  | 114    | s
	107  |  k  | k + 9  | 116    | u
```

### Exploit

To decode the token, a Python script is written to reverse this encoding process. The script iterates over each character of the input string, decreasing its ASCII value by its index to recover the original character:

```python
#!/usr/bin/env python3

import sys

def main():
    encoded_string = sys.argv[1]
    decoded_string = ""

    for index, char in enumerate(encoded_string):
        decoded_string += chr(ord(char) - index)

    print(decoded_string)

if __name__ == "__main__":
    main()

```

Executing this script with the content of the `token` file as input:

```bash
/tmp$ ./reverse.py $(cat ~/token)
f3iji1ju5yuevaus41q1afiuq
```

```bash
flag09@SnowCrash:~$ su flag09
Password: f3iji1ju5yuevaus41q1afiuq
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z

```